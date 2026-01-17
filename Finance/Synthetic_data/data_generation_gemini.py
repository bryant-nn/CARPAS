import json
import time
import os
from typing import List, Dict
import openai
from google import genai
import random
import secrets
from tqdm import tqdm
from report_template import report_template_dict
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

        for key, value in report_template_dict.items():
            if key == "P&L (profit and loss statement) highlights result for this quarter":
                # Include all five aspects from this key
                num_to_pick = secure_rand.randint(1, len(value))

                selected_aspects.extend(secure_rand.sample(value, num_to_pick))
            else:
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
        prompt = f"""You are a financial analyst helping generate synthetic financial content. 
Write a highly detailed and plausible explanation about the following financial aspect as if it were presented: "{aspect}". 
Include fictional but realistic figures, trends, technical initiatives, regional commentary, and strategic insights. Be as specific as possible."""
        
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
        # print(f"Sample {i+1}:")
        # print(f"Randomly selected aspects: {random_aspect}")
        # Phase 1: Generate and save synthetic article


        output_path = os.path.join(output_folder, f"sample_{index}.json")
        
        while(os.path.exists(output_path)):
            index += 1
            output_path = os.path.join(output_folder, f"sample_{index}.json")

        random.seed(index)

        
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