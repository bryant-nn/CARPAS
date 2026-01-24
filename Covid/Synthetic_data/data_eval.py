import os
import json
from typing import List, Tuple
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import jaccard_score
from FlagEmbedding import BGEM3FlagModel
from evaluate import load
import nltk
nltk.download("punkt")

def load_texts_from_json(folder_path: str, content_key: str = 'document') -> Tuple[List[str], List[str]]:
    """
    Load texts and identifiers from JSON files in a folder.

    Args:
        folder_path (str): Path to the folder containing JSON files.
        content_key (str): The key to extract text content from each JSON file. Defaults to 'document'.

    Returns:
        Tuple[List[str], List[str]]: A tuple of texts and corresponding file names or IDs.
    """
    texts = []
    ids = []


    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)

                 # Check for aspect summary rejection
                aspect_summary = data.get("aspect_summary", {})
                if any( ("does not" in summary.lower() or "not metion" in summary.lower() ) for summary in aspect_summary.values()):
                    continue  # Skip this file

                content = data.get(content_key, '').strip()

                if content:
                    texts.append(content)
                    ids.append(filename)
    return texts, ids

def compute_pairwise_bleu_matrix(texts: List[str], max_order: int = 4) -> np.ndarray:
    """
    Compute pairwise BLEU similarity scores across all texts.
    Each cell [i][j] is the BLEU score of text i with text j as reference.

    Args:
        texts (List[str]): List of document texts.
        max_order (int): BLEU n-gram order (default: 4)

    Returns:
        np.ndarray: BLEU similarity matrix.
    """
    bleu = load("bleu")
    n = len(texts)
    sim_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            score = bleu.compute(
                predictions=[texts[i]],
                references=[[texts[j]]],
                max_order=max_order,
            )
            sim_matrix[i][j] = score["bleu"]
            # print(f"BLEU score between text {i} and text {j}: {sim_matrix[i][j]:.4f}")

    return sim_matrix

def compute_pairwise_jaccard(texts: List[str]) -> np.ndarray:
    """
    Compute pairwise Jaccard similarity scores across all texts based on unigrams.

    Args:
        texts (List[str]): List of document texts.

    Returns:
        np.ndarray: Jaccard similarity matrix.
    """
    vectorizer = CountVectorizer(binary=True, stop_words='english')
    binary_matrix = vectorizer.fit_transform(texts).toarray()
    n = len(texts)
    sim_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            score = jaccard_score(binary_matrix[i], binary_matrix[j])
            sim_matrix[i][j] = score
            sim_matrix[j][i] = score
    return sim_matrix

def compute_bge_embeddings(
    texts: List[str],
    model_name: str = "BAAI/bge-m3",
    max_length: int = 8192,
    batch_size: int = 12
) -> np.ndarray:
    """
    Compute dense embeddings using BGE-M3 (FlagEmbedding).

    Args:
        texts (List[str]): List of input texts to encode.
        model_name (str): Name of the BGE model (default is "BAAI/bge-m3").
        max_length (int): Maximum token length per document.
        batch_size (int): Batch size for encoding.

    Returns:
        np.ndarray: 2D numpy array of dense embeddings.
    """
    filtered_texts = [t[:11192] for t in texts if t.strip()]
    if not filtered_texts:
        raise ValueError("All texts are empty after stripping whitespace.")

    model = BGEM3FlagModel(model_name, use_fp16=True, cache_dir='./cache')
    results = model.encode(
        filtered_texts,
        batch_size=batch_size,
        max_length=max_length,
    )
    return np.array(results['dense_vecs'])

def  filter_similar_texts(embeddings: np.ndarray, jaccard_matrix: np.ndarray, bleu_matrix: np.ndarray, 
                         bge_threshold: float, jaccard_threshold: float, bleu_threshold: float) -> List[int]:
    """
    Filter out texts that are too similar based on cosine similarity.

    Args:
        embeddings (np.ndarray): Sentence embeddings of the texts.
        threshold (float): Similarity threshold for filtering.

    Returns:
        List[int]: Indices of texts to keep.
    """
    bge_sim_matrix = embeddings @ embeddings.T
    to_keep = []
    skipped = set()
    n = len(embeddings)
    # print(n)

    for i in range(n):
        if i in skipped:
            continue
        to_keep.append(i)
        for j in range(i + 1, n):
            # print(f"sim_matrix{i} {j}: {sim_matrix[i][j]}")
            if bge_sim_matrix[i][j] >= bge_threshold:
                skipped.add(j)
            if jaccard_matrix[i][j] >= jaccard_threshold:
                skipped.add(j)
            if bleu_matrix[i][j] >= bleu_threshold:
                skipped.add(j)

    return to_keep

def save_filtered_jsons(original_folder: str, output_folder: str, filenames: List[str], indices_to_keep: List[int]) -> None:
    """
    Save filtered JSON files to a new directory.

    Args:
        original_folder (str): Path to the folder with original JSON files.
        output_folder (str): Path to save filtered JSON files.
        filenames (List[str]): List of original filenames.
        indices_to_keep (List[int]): Indices of files to keep.
    """
    os.makedirs(output_folder, exist_ok=True)

    for idx in indices_to_keep:
        filename = filenames[idx]
        with open(os.path.join(original_folder, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        

def filter_near_duplicate_jsons(input_dir: str, output_dir: str, bge_threshold: float, jaccard_threshold: float, bleu_threshold: float) -> None:
    """
    Complete pipeline to load JSONs, filter similar texts, and save results.

    Args:
        input_dir (str): Path to input JSON folder.
        output_dir (str): Path to save filtered JSONs.
        threshold (float): Similarity threshold for filtering.
    """
    texts, ids = load_texts_from_json(input_dir)

    
    bleu_matrix = compute_pairwise_bleu_matrix(texts)
    jac_matrix = compute_pairwise_jaccard(texts)
    embeddings = compute_bge_embeddings(texts=texts, max_length=10000, batch_size=6)
    to_keep = filter_similar_texts(embeddings, jac_matrix, bleu_matrix, bge_threshold, jaccard_threshold, bleu_threshold)
    save_filtered_jsons(input_dir, output_dir, ids, to_keep)

    print(f"Total documents: {len(texts)}")
    print(f"Documents kept: {len(to_keep)}")

if __name__ == "__main__":
    input_directory = "./gemini-2.0-flash"
    output_directory = "./gemini_filtered_data"
    bge_threshold = 0.85
    jaccard_threshold = 0.45
    bleu_threshold = 0.3

    for i in range(4, 5):
        input_directory = f"./gemini-2.0-flash/{i}"
        output_directory = f"./gemini_filtered_data/{i}"
        filter_near_duplicate_jsons(input_directory, output_directory, bge_threshold, jaccard_threshold, bleu_threshold)