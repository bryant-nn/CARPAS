import json
import time
import os
import glob
import argparse
import random
import re 
from typing import List, Dict, Tuple
import openai
from tqdm import tqdm
from collections import defaultdict

from dotenv import load_dotenv
from report_template import report_template_dict
from transcript_template import transcript_template_dict 

load_dotenv()

# ========== Load LLM Client ==========
def load_client(model):
    """
    Loads the appropriate LLM client based on the model name.
    - OpenAI models (gpt/o1/o3) use OpenAI API
    - All other models (including Gemini) use OpenRouter API
    """
    if 'gpt' in model.lower() or 'o1' in model.lower() or 'o3' in model.lower():
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        api_base = "https://api.openai.com/v1"
        client = openai.OpenAI(api_key=api_key, base_url=api_base)
    else:
        # All other models (Gemini, Claude, Llama, Mistral, etc.) via OpenRouter
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable not set.")
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
    return client

# ========== Utility: call OpenAI ChatCompletion ==========
def _chat_completion(prompt: str, model: str, max_retries: int, temperature: float) -> str:
    """
    Handles calling the OpenAI ChatCompletion API with retry logic.
    """
    client = load_client(model)
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()
        except openai.APIError as e:
            print(f"OpenAI API Error (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt) # Exponential backoff
        except Exception as e:
            print(f"An unexpected error occurred (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt) # Exponential backoff
    return "" # Should not reach here if max_retries > 0 and error occurs

# ========== Detailed Aspect Descriptions ==========
def generate_detailed_aspect_descriptions(
    aspects: List[str], 
    model: str = "gpt-4o", 
    max_retries: int = 2, 
    temperature: float = 0.8,
    base_descriptions: Dict[str, str] = None 
) -> Dict[str, str]:
    """
    Generates highly detailed, plausible explanations for a list of financial aspects
    using an LLM, potentially extending from provided base descriptions.
    """
    detailed_descriptions = {}
    for aspect in aspects:
        base_desc = base_descriptions.get(aspect, "") if base_descriptions else ""
        
        prompt = f"""You are a financial analyst helping generate synthetic financial content. 

Write a highly detailed and plausible explanation about the following financial aspect as if it were presented: \"{aspect}\". 

"""
        if base_desc:
            prompt += f"**Based on the following brief summary about this aspect:**\n\"{base_desc}\"\n\n"
            prompt += "Elaborate significantly on this summary. Include fictional but realistic figures, percentages (e.g., 'a 15% increase in Q3 revenue year-over-year to $2.3 billion'), specific trends, technical initiatives, regional commentary, and strategic insights. Be as specific and detailed as possible, **extending from the provided summary** rather than just repeating it.\n"
        else:
            prompt += "Include fictional but realistic figures, percentages (e.g., 'a 15% increase in Q3 revenue year-over-year to $2.3 billion'), specific trends, technical initiatives, regional commentary, and strategic insights. Be as specific as possible."

        response = _chat_completion(prompt=prompt, model=model, max_retries=max_retries, temperature=temperature)
        detailed_descriptions[aspect] = response
    return detailed_descriptions

# ========== Generate Transcript from Aspects ==========
def generate_transcript_from_aspects_llm(
    template: str,
    aspects: List[str],
    aspect_descriptions: Dict[str, str],
    model: str = "gpt-4o",
    temperature: float = 0.7,
    max_retries: int = 2
) -> str:
    """
    Generates a realistic, synthetic earnings call transcript by fully incorporating
    detailed aspect descriptions into a structured template.
    """
    prompt = f"""
You are a financial content writer tasked with generating a realistic, synthetic earnings call transcript that is approximately 3000 to 5000 words.

You will receive:
- A structured **template** outlining the order and roles of speakers (e.g., CEO, CFO, CTO).
- A list of **financial aspects** to be covered.
- A dictionary of **Aspect Descriptions**, which includes detailed narrative content for each aspect. Each entry may include fictional metrics, commentary, strategic initiatives, and regional insights.

Your task is to fully incorporate all content from the Aspect Descriptions dictionary:
- These descriptions are provided for the template’s `"aspect_details"` field and must be treated as the complete content to expand from.
- Write a transcript that sounds like an actual earnings call. It should follow the general structure of the template but feel natural and dynamic.
- **Every description in the Aspect Descriptions dictionary must be completely integrated into the transcript** — this is mandatory. These are not hints or summaries; they are the full content to be paraphrased and embedded into the dialogue.
- Do **not** include bullet points, section titles, or formatting indicators. Write the transcript as pure, flowing dialogue among the participants.
- Ensure that **all** entries from the Aspect Descriptions dictionary are **fully represented and paraphrased** in the dialogue. (it is important)
- These descriptions may be split across different speakers or mentioned in multiple parts of the call, but every part must be covered naturally and completely.
- Use corporate and executive tone. Include references to financial data, strategic initiatives, and regional performance.
- Avoid repetition of phrasing between speakers. Ensure smooth transitions and speaker consistency.
- Never reference or mention “aspects,” “templates,” or any internal structure — let the topics emerge organically in the conversation.
- Template placeholders such as company name, executive names, and product names are flexible — you may assign reasonable fictional values as needed to ensure flow and cohesion.

Return only the full transcript in plain text.

---
**Earnings Call Template (structure only):**
{template}

---
**Aspects to Cover:**
{json.dumps(aspects, indent=2)}

---
**Aspect Descriptions (used to populate `aspect_details`):**
{json.dumps(aspect_descriptions, indent=2)}

---
Before finalizing, review your output and ensure that each aspect description is clearly and fully represented in the transcript. No aspect or description may be omitted. If necessary, revisit earlier sections to integrate any missing content.
Now, generate the full transcript accordingly:
"""
    return _chat_completion(prompt=prompt, model=model, max_retries=max_retries, temperature=temperature)

# ========== Summarization Function 1: Summarize ONLY EXISTING Aspects ==========
def summarize_existing_aspects_from_article(
    aspects: List[str],
    model: str,
    article: str,
    max_retries: int = 2,
    temperature: float = 0.7
) -> Dict[str, str]:
    """
    Summarizes aspects that are explicitly mentioned and discussed in the article.
    If an aspect is not found or sufficiently detailed, it is OMITTED from the response.
    Returns a dictionary with cleaned aspect names as keys and their summaries as values.
    """
    aspects_str_for_prompt = "\n".join([f"{a}" for a in aspects]) # No numbers here
    summary_prompt = (
        "You will receive an article delimited by <article></article>. "
        "For each aspect from the list below, write a concise summary that accurately captures what the article says about that aspect. "
        "**If the article does not explicitly mention or provide sufficient detail for an aspect, DO NOT include that aspect in your JSON response.** "
        "Return your answer as pure JSON (no markdown, no extra text) in the form:\n"
        "{\n"
        '  "aspect name": "summary...",\n'
        '  "aspect name": "summary...",\n'
        "  ...\n"
        "}\n\n"
        f"Aspects to summarize:\n{aspects_str_for_prompt}\n\n"
        f"<article>\n{article}\n</article>"
    )

    summary_json_str = _chat_completion(summary_prompt, model, max_retries, temperature)
    summary_json_str = summary_json_str.replace("```json", "").replace("```", "").strip()

    parsed_summary = None
    try:
        parsed_summary = json.loads(summary_json_str)
    except json.JSONDecodeError:
        print(f"Failed to parse JSON from LLM response for summarize_existing_aspects_from_article. Response:\n{summary_json_str}")
        return None 

    cleaned_aspect_summary = {}
    if parsed_summary:
        for key, value in parsed_summary.items():
            # Clean keys: remove any leading numbers, colons, or extra whitespace
            cleaned_key = re.sub(r'^\s*\d+:\s*', '', key).strip()
            cleaned_aspect_summary[cleaned_key] = value
            
    return cleaned_aspect_summary # Return dictionary with only found aspects

# ========== Summarization Function 2: Summarize ALL REQUESTED Aspects ==========
def summarize_all_requested_aspects_from_article(
    aspects: List[str],
    model: str,
    article: str,
    max_retries: int = 2,
    temperature: float = 0.7
) -> Dict[str, str]:
    """
    Summarizes all provided aspects from the article.
    Guarantees that ALL aspects from the input list are present as keys in the returned dictionary.
    If an aspect is not found or sufficiently detailed, its value will be an empty string.
    Returns a dictionary with cleaned aspect names as keys and their summaries as values (or empty string).
    """
    # Prompt now explicitly asks for clean keys and to include all aspects, filling with empty string if not found.
    aspects_str_for_prompt = "\n".join([f"{a}" for a in aspects]) # No numbers here
    summary_prompt = (
        "You will receive an article delimited by <article></article>. "
        "For each aspect listed below, write a concise summary that accurately captures what the article says about that aspect. "
        "Return your answer as pure JSON (no markdown, no extra text) in the form:\n"
        "{\n"
        '  "aspect name": "summary...",\n'
        '  "aspect name": "summary...",\n'
        "  ...\n"
        "}\n\n"
        f"Aspects:\n{aspects_str_for_prompt}\n\n"
        f"<article>\n{article}\n</article>"
    )

    summary_json_str = _chat_completion(summary_prompt, model, max_retries, temperature)
    summary_json_str = summary_json_str.replace("```json", "").replace("```", "").strip()

    parsed_summary = None
    try:
        parsed_summary = json.loads(summary_json_str)
    except json.JSONDecodeError:
        print(f"Failed to parse JSON from LLM response for summarize_all_requested_aspects_from_article. Response:\n{summary_json_str}")
        return None 

    final_aspect_summary = {}
    if parsed_summary:
        for key, value in parsed_summary.items():
            # Clean keys: remove any leading numbers, colons, or extra whitespace
            cleaned_key = re.sub(r'^\s*\d+:\s*', '', key).strip()
            final_aspect_summary[cleaned_key] = value
    
    # Final safeguard: ensure all requested aspects are indeed present as keys
    for aspect in aspects:
        if aspect not in final_aspect_summary:
            final_aspect_summary[aspect] = "" # Fill with empty string if LLM missed it

    return final_aspect_summary


# ========== Main Execution Logic ==========
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic earnings call data (document, aspects, summary) based on predefined aspects from real transcripts, prioritizing specific aspect counts.")
    parser.add_argument("--model", type=str, default="gemini-2.0-flash", help="LLM model to use for all generation and summarization tasks (e.g., 'gemini-1.5-flash' or 'gpt-4o').")
    parser.add_argument("--input_folder", type=str, default="../data/transcript", help="Path to the folder containing original earnings call transcript JSON files.")
    parser.add_argument("--output_folder", type=str, default="synthetic_final_dataset", help="Base folder to save the train.json and test.json files.")
    parser.add_argument("--train_ratio", type=float, default=0.6, help="Ratio of total samples to allocate to the training set (e.g., 0.6 for 75/106 samples).")
    
    args = parser.parse_args()

    random.seed(42)  # For reproducibility

    model = args.model
    input_folder = args.input_folder
    base_output_folder = args.output_folder
    train_ratio = args.train_ratio
    
    # Define the exact distribution required for the samples.
    TARGET_COUNT_PER_ASPECT_NUM = {
        4: 22,  # 22 samples with 4 aspects
        5: 21,  # 21 samples with 5 aspects
        6: 21,  # 21 samples with 6 aspects
        7: 21,  # 21 samples with 7 aspects
        8: 21   # 21 samples with 8 aspects
    }
    # The total number of samples to generate is the sum of these targets.
    TOTAL_REQUESTED_SAMPLES = sum(TARGET_COUNT_PER_ASPECT_NUM.values()) 

    # Gather all predefined aspects from report_template_dict
    predefined_aspect_pool = list(set(a for sublist in report_template_dict.values() for a in sublist))
    print(f"Loaded {len(predefined_aspect_pool)} predefined aspects from report_template_dict.")

    # Ensure output folder exists and create train/test subfolders
    os.makedirs(base_output_folder, exist_ok=True)
    train_output_subfolder = os.path.join(base_output_folder, "train")
    test_output_subfolder = os.path.join(base_output_folder, "test")
    os.makedirs(train_output_subfolder, exist_ok=True)
    os.makedirs(test_output_subfolder, exist_ok=True)


    # 1. Load all raw transcript files
    transcript_files = glob.glob(os.path.join(input_folder, "*.json"))
    if not transcript_files:
        print(f"No JSON files found in the input folder: {input_folder}. Please ensure your transcripts are in JSON format and have 'symbol' and 'content' keys.")
        exit()

    print(f"Found {len(transcript_files)} raw transcript files.")
    
    raw_transcripts_info = [] # Store original transcript, symbol, and file_path
    for file_path in transcript_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            symbol = data.get('symbol')
            content = data.get('content')

            if not symbol or not content:
                print(f"Warning: 'symbol' or 'content' key missing/empty in {file_path}. Skipping.")
                continue
            raw_transcripts_info.append({"symbol": symbol, "content": content, "file_path": file_path})
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {file_path}: {e}. Skipping.")
        except Exception as e:
            print(f"An unexpected error occurred while reading {file_path}: {e}. Skipping.")

    if not raw_transcripts_info:
        print("No valid raw transcripts loaded. Exiting.")
        exit()

    # Shuffle the raw transcripts to randomize the order of processing and company selection
    random.shuffle(raw_transcripts_info)

    # Prepare the queue of target aspect counts
    target_aspect_counts_queue = []
    for num_aspects, count in TARGET_COUNT_PER_ASPECT_NUM.items():
        target_aspect_counts_queue.extend([num_aspects] * count)
    
    # Shuffle the queue to randomize which aspect count target each transcript attempts to fulfill
    random.shuffle(target_aspect_counts_queue)

    # Initialize counters for generated samples
    generated_train_count = 0
    generated_test_count = 0
    
    # Dictionaries to hold final reporting data (company and aspect counts)
    final_distribution_report_by_aspect_num = defaultdict(lambda: {'train': 0, 'test': 0})
    final_distribution_report_by_company = defaultdict(lambda: {'train': 0, 'test': 0})

    print(f"\nStarting synthetic data generation for up to {TOTAL_REQUESTED_SAMPLES} samples...")
    
    # Use tqdm for overall progress through the synthesis of samples
    pbar_synthetic = tqdm(total=TOTAL_REQUESTED_SAMPLES, desc="Generating Synthetic Data")

    # Iterate through each shuffled raw transcript
    for i, transcript_data in enumerate(raw_transcripts_info):
        # Stop if we have generated all required samples
        if generated_train_count + generated_test_count >= TOTAL_REQUESTED_SAMPLES:
            pbar_synthetic.close()
            break

        # Check if we have a target aspect count available for this iteration
        if i >= len(target_aspect_counts_queue):
            print("\nWarning: All target aspect count slots have been assigned. Stopping generation early.")
            break # No more specific aspect counts to assign
        
        current_target_aspect_num = target_aspect_counts_queue[i] # Get the target for this iteration

        original_doc = transcript_data['content']
        company_symbol = transcript_data['symbol']
        original_file_path = transcript_data['file_path'] 
        
        # Phase 1: Summarize existing aspects from the original transcript
        # Use summarize_existing_aspects_from_article which OMITS unmentioned aspects
        aspect_summary_from_real = summarize_existing_aspects_from_article(
            aspects=predefined_aspect_pool, # Use the full pool for initial analysis
            article=original_doc,
            model=model
        )
        
        if aspect_summary_from_real is None: # LLM parsing failed
            pbar_synthetic.set_description(f"Skipping {company_symbol} (LLM summary failed for original doc)")
            continue 

        all_discussed_aspects_in_real = list(aspect_summary_from_real.keys())
        
        # Check if the raw transcript has enough actual discussed aspects to fulfill the current target_aspect_num
        if len(all_discussed_aspects_in_real) < current_target_aspect_num:
            pbar_synthetic.set_description(f"Skipping {company_symbol} (Too few aspects for target {current_target_aspect_num})")
            continue 

        # Randomly sample the required number of aspects from those found in the real transcript
        selected_aspects_for_this_sample = random.sample(all_discussed_aspects_in_real, current_target_aspect_num)
        
        # Create the initial summaries for *only* these selected aspects to pass for extension
        selected_aspects_base_summary = {
            aspect: aspect_summary_from_real[aspect] 
            for aspect in selected_aspects_for_this_sample
        }

        # Phase 2: Generate synthetic document and final summary
        
        # Get template for this number of aspects
        template_key = str(current_target_aspect_num)
        template = transcript_template_dict.get(template_key)
        if not template:
            print(f"\nWarning: No transcript template found for {current_target_aspect_num} aspects (key '{template_key}'). Skipping sample from {company_symbol}.")
            pbar_synthetic.set_description(f"Skipping {company_symbol} (Template missing for {current_target_aspect_num} aspects)")
            continue 
        
        pbar_synthetic.set_description(f"Generating for {company_symbol} ({current_target_aspect_num} aspects)")

        # Generate detailed descriptions for these aspects, *extending from initial summaries*
        detailed_aspect_descs = generate_detailed_aspect_descriptions(
            aspects=selected_aspects_for_this_sample,
            model=model,
            base_descriptions=selected_aspects_base_summary # Pass the initial summaries here
        )
        
        # Generate the full synthetic transcript (document)
        synthetic_transcript_doc = generate_transcript_from_aspects_llm(
            template=template,
            aspects=selected_aspects_for_this_sample, 
            aspect_descriptions=detailed_aspect_descs,
            model=model
        )
        
        if not synthetic_transcript_doc:
            print(f"\nWarning: Failed to generate synthetic transcript for sample from {company_symbol}. Skipping.")
            pbar_synthetic.set_description(f"Skipping {company_symbol} (Synthetic transcript gen failed)")
            continue

        # Generate the final aspect-based summary from the *synthetic* document
        # Use summarize_all_requested_aspects_from_article which ensures all aspects are present as keys
        final_aspect_summary = summarize_all_requested_aspects_from_article(
            aspects=selected_aspects_for_this_sample, # Use the selected aspects here (they are the target aspects for the synthetic doc)
            article=synthetic_transcript_doc,
            model=model
        )
        
        if final_aspect_summary is None: 
            print(f"\nWarning: Failed to parse final aspect summary from synthetic transcript for {company_symbol}. Skipping.")
            pbar_synthetic.set_description(f"Skipping {company_symbol} (Final summary parse failed)")
            continue
        
        # --- Quality Check for final_aspect_summary completeness ---
        # Ensure the number of keys in final_aspect_summary matches the number of aspects requested.
        # This verifies that LLM followed the instruction to include all keys, even if empty.
        # It also implicitly checks if unexpected extra keys were added.
        if len(final_aspect_summary) != len(selected_aspects_for_this_sample):
            print(f"\nWarning: Final aspect summary for {company_symbol} has {len(final_aspect_summary)} aspects, but {len(selected_aspects_for_this_sample)} were expected. Skipping this sample due to inconsistency.")
            print(f"  Expected Aspects: {selected_aspects_for_this_sample}")
            print(f"  Actual Summary Keys: {list(final_aspect_summary.keys())}")
            pbar_synthetic.set_description(f"Skipping {company_symbol} (Final summary key mismatch/incomplete)")
            continue
        # --- END Quality Check ---

        # Prepare the final output structure for this sample
        final_sample_data = {
            "document": synthetic_transcript_doc,
            "aspects": selected_aspects_for_this_sample, # This list is already clean
            "aspect_summary": final_aspect_summary # This dict has clean keys and matched count now
        }
        
        # Determine if it goes to train or test and save immediately
        output_subfolder_path = ""
        set_type = ""
        if generated_train_count < int(TOTAL_REQUESTED_SAMPLES * train_ratio):
            output_subfolder_path = train_output_subfolder
            set_type = "train"
            generated_train_count += 1
        else:
            output_subfolder_path = test_output_subfolder
            set_type = "test"
            generated_test_count += 1
        
        # Generate a unique filename for the saved JSON
        # Format: CompanySymbol_AspectsNum_SetType_Index.json
        global_file_index = generated_train_count + generated_test_count # A simple overall counter
        output_filename = f"{company_symbol}_{current_target_aspect_num}aspects_{set_type}_{global_file_index:03d}.json"
        output_path = os.path.join(output_subfolder_path, output_filename)
        
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(final_sample_data, f, ensure_ascii=False, indent=2)
            
            # Update reporting counts for successfully saved sample
            final_distribution_report_by_aspect_num[current_target_aspect_num][set_type] += 1
            final_distribution_report_by_company[company_symbol][set_type] += 1

            pbar_synthetic.update(1) # Increment tqdm for each successfully generated and saved sample
        except Exception as e:
            print(f"\nError saving file {output_path}: {e}. This sample will not be included in final counts.")
            # If save fails, this sample wasn't fully processed/saved, so decrement its respective counter
            if set_type == "train": generated_train_count -= 1
            else: generated_test_count -= 1
        
        time.sleep(1) # Delay between LLM calls

    pbar_synthetic.close() # Close the tqdm bar at the end
    
    print(f"\nFinished attempting to generate {TOTAL_REQUESTED_SAMPLES} samples.")
    
    # --- Final Dataset Distribution Summary ---
    total_generated_train_final = sum(d['train'] for d in final_distribution_report_by_aspect_num.values())
    total_generated_test_final = sum(d['test'] for d in final_distribution_report_by_aspect_num.values())

    print("\n--- Final Dataset Distribution Summary ---")
    print("\nDistribution by Aspect Count (Actual Generated Samples):")
    for aspect_n in sorted(TARGET_COUNT_PER_ASPECT_NUM.keys()):
        train_count = final_distribution_report_by_aspect_num[aspect_n]['train']
        test_count = final_distribution_report_by_aspect_num[aspect_n]['test']
        target_count = TARGET_COUNT_PER_ASPECT_NUM.get(aspect_n, 0)
        print(f"  Aspects {aspect_n}: Train: {train_count}, Test: {test_count} (Target Total for this aspect count: {target_count})")
    
    print("\nDistribution by Company (Actual Generated Samples):")
    all_companies_in_output = sorted(final_distribution_report_by_company.keys())
    if not all_companies_in_output:
        print("  No companies generated samples.")
    else:
        for company in all_companies_in_output:
            train_count = final_distribution_report_by_company[company]['train']
            test_count = final_distribution_report_by_company[company]['test']
            print(f"  Company {company}: Train: {train_count}, Test: {test_count} (Total: {train_count + test_count})")

    print(f"\nTotal Train Samples Generated: {total_generated_train_final} (Approximate Target: {int(TOTAL_REQUESTED_SAMPLES * train_ratio)})")
    print(f"Total Test Samples Generated: {total_generated_test_final} (Approximate Target: {TOTAL_REQUESTED_SAMPLES - int(TOTAL_REQUESTED_SAMPLES * train_ratio)})")
    print(f"Total Samples Generated: {total_generated_train_final + total_generated_test_final} (Overall Target: {TOTAL_REQUESTED_SAMPLES})")

    if total_generated_train_final + total_generated_test_final < TOTAL_REQUESTED_SAMPLES:
        print("\nNote: The total generated sample count is less than the target. This indicates that the available raw transcripts did not yield enough suitable samples (i.e., transcripts with enough discussed aspects to fulfill the assigned target aspect count), or LLM generation/summarization steps failed for some samples.")

    print("\nProcessing complete. Check the output folder for your generated data files.")