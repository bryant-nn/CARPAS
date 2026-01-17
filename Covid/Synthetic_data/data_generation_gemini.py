import json
import time
import os
from typing import List, Dict
import openai
from google import genai
import random
import secrets
from tqdm import tqdm
from report_template import epidemic_report_template_dict
from transcript_template import transcript_template_dict
import argparse

from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
def load_client(model):
    if 'gpt' in model:
        api_key = os.getenv("OPENAI_API_KEY")
        api_base = "https://api.openai.com/v1"
        client = openai.OpenAI(api_key=api_key, base_url=api_base)
    elif 'gemini' in model:
        api_key = os.getenv("GEMINI_API_KEY")
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    return client

# ========== Utility: call OpenAI ChatCompletion ==========
def _chat_completion(prompt: str, model: str, max_retries: int, temperature: float) -> str:
    """
    Internal helper to query the OpenAI ChatCompletion API with retries.
    """
    client = load_client(model)
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                # max_tokens=8192, 
                # logprobs=True,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Error: {e}. Retrying {attempt + 1}/{max_retries}...")
            time.sleep(2)

def generate_aspect_sets(num_samples=10, aspect_num = 4):
    all_aspect_sets = []
    secure_rand = secrets.SystemRandom()

    for _ in range(num_samples):
        selected_aspects = []

        for key, value in epidemic_report_template_dict.items():
            
            # Only pick one aspect randomly from this key
            if isinstance(value, list):
                selected_aspects.append(secure_rand.choice(value))
            else:
                selected_aspects.append(value)

        random.shuffle(selected_aspects)
        if random.choice([True, False]):
            selected_aspects.reverse()

        sampled = random.sample(selected_aspects, k=min(aspect_num, len(selected_aspects)))
        random.shuffle(sampled)

        all_aspect_sets.append(sampled)

    return all_aspect_sets

# === Generate detailed description for each aspect ===
def generate_detailed_aspect_descriptions(aspects: List[str], model: str = "gpt-4o", max_retries: int = 2, temperature: float = 0.8) -> Dict[str, str]:
    detailed_descriptions = {}
    for aspect in aspects:
        prompt = f"""You are an expert in epidemiology helping generate synthetic content for a COVID-19 press briefing. 
Write a highly detailed and realistic explanation about the following aspect of the epidemic: "{aspect}". 
Include plausible numbers, trends, actions, and government responses. Describe regional variations, changes in policies, and medical resource status. Be as specific and detailed as possible."""
        
        response = _chat_completion(prompt=prompt, model=model, max_retries=max_retries, temperature=temperature)
        # print(f"Aspect: {aspect}\nResponse: {response}\n")
        detailed_descriptions[aspect] = response
    return detailed_descriptions

def generate_transcript_from_aspects_llm(
    template: str,
    aspects: List[str],
    aspect_descriptions: Dict[str, str],
    model: str = "gpt-4o",
    temperature: float = 0.7,
    max_retries: int = 2
) -> str:
    
    prompt = f"""
You are a professional scriptwriter tasked with generating a realistic, synthetic epidemic press conference transcript.

You will receive:
- A structured **template** outlining the order and speakers (e.g., health officials, epidemiologists, government leaders).
- A list of **epidemic aspects** to be discussed (such as COVID case counts, vaccination progress, regional outbreaks, healthcare system capacity).
- A dictionary of **Aspect Descriptions**, which includes detailed narrative content for each aspect. These descriptions are detailed and must be fully integrated into the conversation.

Write a transcript that flows naturally, with each aspect description fully incorporated into the dialogue. Use professional and authoritative language, as would be used in a public health press briefing. Avoid repetition and ensure smooth transitions between speakers.

### Key Instructions:
1. Write a transcript that sounds like an actual **epidemic press conference**. 
2. This should follow the general structure of the provided **template** but should feel natural, dynamic, and organic.
3. Every description in the **Aspect Descriptions dictionary** must be completely integrated into the transcript. This means each entry must be paraphrased, reworded, and woven into the dialogue without omitting any information. **It is mandatory that all content be fully represented**.
4. Do **not** include bullet points, section titles, or formatting indicators. The transcript should be pure, flowing dialogue.
5. Ensure that all entries from the **Aspect Descriptions** dictionary are fully integrated. This may involve splitting the descriptions across different speakers or different parts of the conversation, but **every part must be mentioned naturally and completely**.
6. The tone should be **corporate and authoritative**, with references to public health data, government policies, regional performance, and actions being taken. Think of this as a **real press conference** where multiple officials are giving an update.
7. The **transitions between speakers** should be smooth, and the dialogue should reflect an organized flow of information. Avoid repetition of phrases between speakers.
8. **Never reference** or mention the terms “aspects,” “templates,” or any internal structure. The topics and aspects should naturally emerge as part of the conversation without directly labeling them as such.
9. **Template placeholders** such as country/region names, official titles, or numbers (like case counts or vaccine doses) should be filled with **fictional but realistic values** that maintain the **natural flow** of the conversation.

Return only the full transcript in plain text.

---
**Press Conference Template (structure only):**
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

def generate_aspect_summaries_from_aspects_llm(
    aspects: List[str],
    model: str = "gpt-4o",
    max_retries: int = 2,
    temperature: float = 0.7,
    article: str = "",
    output_path: str = "aspect_summaries.json"
):
    aspects_str = "\n".join([f"{i+1}: {a}" for i, a in enumerate(aspects)])

    summary_prompt = (
        "You will receive an article delimited by <article></article>. "
        "For each aspect listed below, write a concise summary that accurately captures what the article says about that aspect. "
        "Return your answer as pure JSON (no markdown, no extra text) in the form:\n"
        "{\n"
        '  "aspect name": "summary...",\n'
        '  "aspect name": "summary...",\n'
        "  ...\n"
        "}\n\n"
        f"Aspects:\n{aspects_str}\n\n"
        f"<article>\n{article}\n</article>"
    )

    summary_json_str = _chat_completion(summary_prompt, model, max_retries, temperature)
    summary_json_str = summary_json_str.replace("```", "").replace("json", "")

    # Try to parse the JSON response from the model
    try:
        aspect_summary = json.loads(summary_json_str)
    except json.JSONDecodeError:
        print("Failed to parse JSON response from the model. Please check the output.")
        print(f"Response was:\n{summary_json_str}")
        return

    # Save article and aspects to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"document": article, "aspects": aspects, "aspect_summary": aspect_summary}, f, ensure_ascii=False, indent=2)

    return 

# ========== Main ==========
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run aspect summarization.")
    parser.add_argument("--num_sample", type=int, default=2, help="Number of samples to generate")
    parser.add_argument("--num_aspect", type=int, default=2, help="Number of aspects to generate")
    args = parser.parse_args()

    # Phase 0: Get report template's aspects
    num_samples = args.num_sample

    random_aspects = generate_aspect_sets(num_samples=num_samples, aspect_num=args.num_aspect)

    model = "gemini-2.0-flash"

    output_folder = f"{model}/{args.num_aspect}"
    os.makedirs(output_folder, exist_ok=True)

    index = 1

    for _, random_aspect in tqdm(enumerate(random_aspects)):

        output_path = os.path.join(output_folder, f"sample_{index}.json")
        
        while(os.path.exists(output_path)):
            index += 1
            output_path = os.path.join(output_folder, f"sample_{index}.json")

        # random.seed(index)

        
        # Generate detailed descriptions for each aspect
        aspect_descriptions = generate_detailed_aspect_descriptions(random_aspect, model=model, max_retries=2, temperature=0.7)

        # Generate transcript from aspects using LLM
        template = transcript_template_dict[f"{len(random_aspect)}"]

        transcript = generate_transcript_from_aspects_llm(
            template=template,
            aspects=random_aspect,
            aspect_descriptions=aspect_descriptions,
            model=model,
            temperature=0.7,
            max_retries=2
        )

        generate_aspect_summaries_from_aspects_llm(model=model, aspects=random_aspect, article=transcript, output_path=output_path, max_retries=2, temperature=0.7)