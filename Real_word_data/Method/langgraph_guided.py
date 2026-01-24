import os
import json
import json5
import random
import argparse
from dotenv import load_dotenv
from typing import TypedDict, List
from tqdm import tqdm
import re
import openai
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from eval import evaluate_summary
import ast
import time
from collections import deque
import tiktoken
import pandas as pd

# ========== 0. Load ENV ==========
load_dotenv()

# Record the time and token usage for each API call
token_window = deque()
TOKEN_LIMIT_PER_MIN = 12000

def wait_for_token_budget(tokens_needed: int):
    now = time.time()

    while token_window and now - token_window[0][0] > 61:
        token_window.popleft()

    current_total = sum(t[1] for t in token_window)

    if current_total + tokens_needed > TOKEN_LIMIT_PER_MIN:
        wait_time = 60 - (now - token_window[0][0])
        time.sleep(wait_time + 10)

def record_token_usage(tokens_used: int):
    token_window.append((time.time(), tokens_used))

def estimate_tokens(text, model="gpt-4o"):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

# ========== 1. Model Initialization ==========
def load_llm(model_name: str, temperature: float = 0.7, _api_key: str = None):
    
    if 'gpt' in model_name or 'o3' in model_name:
        api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = api_key
        openai.api_base = "https://api.openai.com"
        
        global TOKEN_LIMIT_PER_MIN
        TOKEN_LIMIT_PER_MIN = 3000000000  # Set a higher limit for OpenAI

        if 'o3' in model_name:
            # For O3 models, use the OpenAI API with the o3 model name
            return ChatOpenAI(model_name=model_name, openai_api_key=api_key, temperature=1)
        
        return ChatOpenAI(model_name=model_name, openai_api_key=api_key, temperature=temperature)
    elif 'llama' in model_name:
        api_key = os.getenv("GROQ_API_KEY2")

        return ChatGroq(model=model_name, groq_api_key=api_key, temperature=temperature)
    elif 'gemini' or "gemma" in model_name:
        api_key = os.getenv(_api_key)
        os.environ["GOOGLE_API_KEY"] = api_key
        return ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
    

def predict_num_aspects(article: str, model: str = "gpt-4o", temperature: float = 0.7):
    prompt = f"""
You are given a financial article. Estimate how many distinct, non-overlapping aspects or key themes are discussed in the article. Only return a single integer representing the number of aspects.

Article:
{article}
"""
    tokens_needed = estimate_tokens(prompt, model)
    wait_for_token_budget(tokens_needed + 500)

    response = llm.invoke([HumanMessage(content=prompt)])
    result = response.content.strip()

    match = re.search(r"\d+", result)
    count = int(match.group(0))

    if 'token_usage' in response.response_metadata:
        tokens = response.response_metadata['token_usage']['total_tokens']
    else:
        tokens = response.usage_metadata['total_tokens']
    record_token_usage(tokens)

    return count, tokens


# ========== 2. Memory Initialization ==========
memory = MemorySaver()
store = InMemoryStore()

# ========== 3. State Schema ==========
class SummaryState(TypedDict):
    article: str
    aspects: List[str]
    revised_aspects: List[List[str]]
    summaries: dict
    complete: bool
    steps: int
    tokens: int
    count_hint: str

# ========== 4. Node Functions ==========
def check_coverage_fn(state: SummaryState):
    # max steps = 16
    if state.get("steps", 0) >= 14:
        return {**state, "complete": True, "steps": state.get("steps", 0) + 1}
    
    #You are given an article and a list of aspect titles. Your task is to decide whether these aspects better reflect the key themes and cover almost all the key content of the article.
    #better reflect the key themes or main topics.
    prompt = f"""
You are given an article and a list of aspect titles. Your task is to decide whether these aspects better reflect the key themes and cover the main topics of the article.
{state.get("count_hint", "").replace("- ", "")}

If yes, answer only: YES
If not, answer only: NO

Article:
"{state['article']}"

Aspects:
{json.dumps(state['aspects'], indent=2)}
"""
    # print(f"prompt: {prompt}")
    estimate_prompt_tokens = estimate_tokens(prompt)
    estimated_tokens = estimate_prompt_tokens + 1500  # prompt word count + buffer
    wait_for_token_budget(estimated_tokens)

    first_response = llm.invoke([HumanMessage(content=prompt)])
    response = first_response.content.strip().upper()
    
    if 'token_usage' in first_response.response_metadata:
        tokens = first_response.response_metadata['token_usage']['total_tokens']
    else:
        tokens = first_response.usage_metadata['total_tokens']

    record_token_usage(tokens)

    return {**state, "complete": response == "YES" or ("YES" in response and "NO" not in response), "steps": state.get("steps", 0) + 1, "tokens": state.get("tokens", 0) + tokens}

check_coverage = RunnableLambda(check_coverage_fn)


def revise_aspects_fn(state: SummaryState):
    keys = store.get("aspect_examples_index", "keys") or []
    keys = list(keys) if isinstance(keys, list) else []
    past = [store.get("aspect_examples", k) for k in keys]
    sampled = random.sample(past, k=min(2, len(past)))

    mem_text = "\n\n".join([
        f"Article: {json.dumps(p['article'])}\nGround Truth Aspects: {json.dumps(p['ground_truth'])}\n" for p in sampled
    ]) if sampled else "(no memory available)"

    if sampled:
        prompt = f"""
Revise the following aspects to better reflect the important content of the article.
You may **retain**, **delete**, **modify**, or **add** aspects. Only return the updated list of aspect titles as a list.

Article:
"{state['article']}"

Original Aspects:
{json.dumps(state['aspects'], indent=2)}

Here are some past examples:
{mem_text}
"""
    else:
        prompt = f"""
You are given a financial article and an initial list of section titles (called "aspects"). Your task is to revise this list to better reflect the key themes and content of the article.

Instructions:

1. For each aspect in the **provided list**, perform the following:
- Label it as:
    - **Retain** if it is well-phrased, specific, and clearly supported by the article.
    - **Modify** if it is relevant but needs rephrasing or more specific focus.
    - **Delete** if it is irrelevant, redundant, or unsupported by the article.

2. Identify any **new aspects** that are important but missing from the provided list:
- Clearly name the new aspect.
- Summarize what the article says about it.

Guidelines:
- Ensure aspects are **clear, specific, and non-overlapping**.
{state.get("count_hint", "")}

Article:
"{state['article']}"

Original Aspects:
{json.dumps(state['aspects'], indent=2)}

Only return the updated list of aspect titles in the following list format:
{[
  "aspect_0", "aspect_1", "aspect_2", ...
]}
"""

    estimate_prompt_tokens = estimate_tokens(prompt)
    estimated_tokens = estimate_prompt_tokens + 2500  # prompt word count + buffer
    wait_for_token_budget(estimated_tokens)

    # print("🔄 Revising aspects...")
    # print(f"🔄 Prompt:\n{prompt}")

    first_response = llm.invoke([HumanMessage(content=prompt)])
    # print(f"🔄 Model Response:\n{first_response.content.strip()}")
    response = first_response.content.strip().replace("```json", "").replace("```", "")

    if 'token_usage' in first_response.response_metadata:
        tokens = first_response.response_metadata['token_usage']['total_tokens']
    else:
        tokens = first_response.usage_metadata['total_tokens']
    
    record_token_usage(tokens)

    match = re.search(r"\[.*?\]", response, re.DOTALL)

    revised = ast.literal_eval(match.group(0))

    # time.sleep(60)

    return {
        **state,
        "revised_aspects": state.get("revised_aspects", []) + [state["aspects"]],
        "aspects": revised,
        "steps": state.get("steps", 0) + 1,
        "tokens": state.get("tokens", 0) + tokens
    }


revise_aspects = RunnableLambda(revise_aspects_fn)


def summarize_aspects_fn(state: SummaryState):
    prompt = f"""
You are given an article and a list of finalized aspects. Write a concise summary for each aspect based on the article.

Article:
"{state['article']}"

Aspects:
{json.dumps(state['aspects'], indent=2)}

Please only return your output in the following JSON format:
{{
  "aspect_name": "summary text...",
  "aspect_name": "summary text...",
  ...
}}
""".strip()
    
    estimate_prompt_tokens = estimate_tokens(prompt)
    estimated_tokens = estimate_prompt_tokens + 2800  # prompt word count + buffer
    wait_for_token_budget(estimated_tokens)
    
    first_response = llm.invoke([HumanMessage(content=prompt)])
    response = first_response.content.strip().replace("```json", "").replace("```", "")
    
    if 'token_usage' in first_response.response_metadata:
        tokens = first_response.response_metadata['token_usage']['total_tokens']
    else:
        tokens = first_response.usage_metadata['total_tokens']

    record_token_usage(tokens)

    # print(f"🔄 Model Response:\n{response}")
    match = re.search(r"\{.*?\}", response, re.DOTALL)

    # print(f"🔄 Model Response:\n{match.group(0)}")
    summaries = ast.literal_eval(match.group(0))

    # time.sleep(40)

    return {**state, "summaries": summaries, "steps": state.get("steps", 0) + 1, "tokens": state.get("tokens", 0) + tokens}

summarize_aspects = RunnableLambda(summarize_aspects_fn)


def route_check(state: SummaryState) -> str:
    return "summarize" if state.get("complete", False) else "revise"

# ========== 5. Build LangGraph Workflow ==========
def build_workflow(use_memory=True):
    workflow = StateGraph(SummaryState)

    workflow.add_node("check", check_coverage)
    workflow.add_node("revise", revise_aspects)
    workflow.add_node("summarize", summarize_aspects)

    workflow.set_entry_point("check")
    workflow.add_conditional_edges("check", route_check, {"summarize": "summarize", "revise": "revise"})
    workflow.add_edge("revise", "check")
    workflow.set_finish_point("summarize")

    return workflow.compile(checkpointer=memory if use_memory else None)

def load_prediction_csv(path="test_results.csv"):
    df = pd.read_csv(path)
    return dict(zip(df['file_name'], df['prediction']))

# ========== 6. Main Execution Loop ==========
def process_files(folder_path: List[str], all_aspects: List[str], output_path: str, use_memory: bool, y: int, negative: int, 
                  provide_aspect_num: bool, aspect_predictions_map: dict):
    graph = build_workflow(use_memory)

    n = 0
    for file_path in tqdm(folder_path):
        # n += 1
        filename = os.path.basename(file_path)
        if not filename.endswith('.json'):
            continue

        number_aspect = filename.split('_')[1][0]
        output_file = os.path.join(output_path, f"{filename}")

        # output_file = os.path.join(output_path, filename)
        if os.path.exists(output_file):
            continue

        with open(f"../Synthetic_data/synthetic_final_dataset/test/{file_path}", 'r', encoding='utf-8') as f:
            data = json.load(f)

        article = data.get('document', '').strip()
        ground_truth_aspects = data.get('aspects', [])
        ground_truth_summaries = data.get('aspect_summary', {})

        # Sample ground truth aspects and unrelated ones
        provided_aspects = []
        # == true data ==
        if y > 0:
            true_aspects = random.sample(ground_truth_aspects, k=min(y, len(ground_truth_aspects)))
            provided_aspects.extend(true_aspects)    
        # == fake data ==
        if negative > 0:
            candidate_aspects = list(set(all_aspects) - set(ground_truth_aspects))        
            random_aspects = random.sample(candidate_aspects, k=negative)
            provided_aspects.extend(random_aspects)
        
        
        count_hint = ""
        predict_tokens = 0
        predicted_aspect_num = 0
        if provide_aspect_num:
            key_file_path = f"../Synthetic_data/synthetic_final_dataset/test/{file_path}"
            if key_file_path in aspect_predictions_map:
                predicted_aspect_num = aspect_predictions_map[key_file_path]
                count_hint = f"- According to previous prediction, this article likely contains around **{predicted_aspect_num}** aspects. Please take this into account when revising your own aspects."
            else:
                predicted_aspect_num, predict_tokens = predict_num_aspects(article, model=MODEL_NAME)
                count_hint = f"- According to other agents, this article likely contains around **{predicted_aspect_num}** aspects. Please take this into account when revising your own aspects."

        # print(count_hint)

        initial_state = SummaryState(
            article=article,
            aspects=provided_aspects,
            revised_aspects=[],
            summaries={},
            complete=False,
            steps=0,
            tokens=0,
            count_hint=count_hint
        )

        config = {"configurable": {"thread_id": filename}}
        graph_result = graph.invoke(initial_state, config)

        evaluation_result = evaluate_summary(
            list(ground_truth_summaries.values()),
            list(graph_result["summaries"].values())
        )

        # Save ground truth + initial to long-term store
        if use_memory:
            store.put("aspect_examples", filename, {
                "ground_truth": ground_truth_aspects,
                "article": article
            })

            key_list_item = store.get("aspect_examples_index", "keys")
            key_list = key_list_item if isinstance(key_list_item, list) else []
            if filename not in key_list:
                key_list.append(filename)
                store.put("aspect_examples_index", "keys", key_list)

        result = {
            "document": article,
            "ground_truth_aspects": ground_truth_aspects,
            "ground_truth_aspect_summary": ground_truth_summaries,
            "provided_aspects": provided_aspects,
            "generated_prompt_aspect_summary": graph_result["summaries"],
            "pairing": evaluation_result["pairing"],
            "metrics": evaluation_result["metrics"],
            "total_steps": graph_result["steps"],
            "total_tokens": graph_result["tokens"] + predict_tokens,
            "predicted_aspect_num": predicted_aspect_num if provide_aspect_num else 0,
        }

        os.makedirs(output_path, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        # print(f"✅ Processed: {file_path}, Total Steps: {graph_result['steps']}")

        # if n == 10:
        # break

def list_all_json_files(root_dir):
    json_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.json'):
                full_path = os.path.join(dirpath, file)
                json_files.append(full_path)
    return json_files

# ========== 7. Entry Point ==========
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run aspect summarization.")
    parser.add_argument("--memory", type=lambda x: x.lower() == "true", default=False,
                        help="Use Memory: True or False (default: False)")
    parser.add_argument("--y", type=int, default=2, help="Number of true aspects to sample from ground truth")
    parser.add_argument("--n", type=int, default=2, help="Number of unrelated aspects to add")
    parser.add_argument("--model", type=str, default="gpt-4o-mini",
                    help="Model name to use, e.g., 'gpt-4o-mini', 'gpt-4o', 'llama3-70b-8192'")
    parser.add_argument("--provide_aspect_num", action="store_true", help="Predict number of aspects")
    parser.add_argument("--aspect_source", type=str, choices=["predict", "csv"], default="predict")
    parser.add_argument("--api_key", type=str, default="GOOGLE_API_KEY")
    args = parser.parse_args()

    MODEL_NAME = args.model
    llm = load_llm(model_name=MODEL_NAME, _api_key=args.api_key)

    from report_template import report_template_dict

    all_aspects = []
    for key, value in report_template_dict.items():
        all_aspects.extend(value if isinstance(value, list) else [value])


    folder_path = '../Synthetic_data/synthetic_final_dataset/test'
    test_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if args.provide_aspect_num:
        output_folder = f"../Result/langgraph{'_prompt_with_predicted_aspect' if args.aspect_source == "predict" else '_prompt_with_csv_aspect'}/{'use_memory' if args.memory else 'no_memory'}/gemini_filtered_data_y{args.y}n{args.n}/{MODEL_NAME}"
    else:
        output_folder = f"../Result/langgraph/{'use_memory' if args.memory else 'no_memory'}/gemini_filtered_data_y{args.y}n{args.n}/{MODEL_NAME}"
    os.makedirs(output_folder, exist_ok=True)

    aspect_predictions_map = load_prediction_csv() if args.provide_aspect_num and args.aspect_source == "csv" else {}

    process_files(test_files, all_aspects, output_folder, use_memory=args.memory, y=args.y, negative=args.n, provide_aspect_num=args.provide_aspect_num, aspect_predictions_map=aspect_predictions_map)

