"""
Multi-Category Synthetic Data Generation for CARPAS

This script extends the original data generation pipeline to support multiple
industry categories. It generates earnings call transcripts for any of the
20 defined company categories.

Features:
- Equal distribution of aspect counts (4, 5, 6, 7, 8)
- OpenRouter API for all models (including Gemini)
- Pydantic structured output for reliable JSON parsing
"""

import json
import time
import os
import argparse
import random
import secrets
from typing import List, Dict
import openai
from tqdm import tqdm
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()


# ============ Pydantic Models for Structured Output ============

class AspectSummary(BaseModel):
    """Structured output for aspect summaries."""
    summaries: Dict[str, str] = Field(
        description="Dictionary mapping each aspect name to its summary from the transcript"
    )


# ============ API Client ============

def load_client(model: str):
    """
    Loads the appropriate LLM client based on the model name.
    - OpenAI models (gpt/o1/o3) use OpenAI API
    - All other models (including Gemini) use OpenRouter API
    """
    if 'gpt' in model.lower() or 'o1' in model.lower() or 'o3' in model.lower():
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        client = openai.OpenAI(api_key=api_key, base_url="https://api.openai.com/v1")
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


def _chat_completion(prompt: str, model: str, max_retries: int = 3, temperature: float = 0.7) -> str:
    """Call the LLM with retry logic."""
    client = load_client(model)
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Error: {e}. Retrying {attempt + 1}/{max_retries}...")
            time.sleep(2 ** attempt)
    return ""


def _chat_completion_structured(
    prompt: str, 
    model: str, 
    response_model: type[BaseModel],
    max_retries: int = 3, 
    temperature: float = 0.7
) -> BaseModel:
    """
    Call the LLM with structured output using Pydantic model.
    Uses response_format with json_schema for OpenRouter compatibility.
    """
    client = load_client(model)
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": response_model.__name__,
                        "strict": True,
                        "schema": response_model.model_json_schema()
                    }
                }
            )
            # Parse and validate the JSON response using Pydantic
            return response_model.model_validate_json(response.choices[0].message.content)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Error: {e}. Retrying {attempt + 1}/{max_retries}...")
            time.sleep(2 ** attempt)
    return None


# ============ Template Loading ============

def load_category_templates(category_key: str, templates_dir: str = "industry_templates"):
    """
    Load report and transcript templates for a specific category.
    Falls back to default templates if category-specific ones don't exist.
    """
    category_dir = os.path.join(templates_dir, category_key)
    
    report_template_path = os.path.join(category_dir, "report_template.py")
    transcript_template_path = os.path.join(category_dir, "transcript_template.py")
    
    report_template_dict = None
    transcript_template_dict = None
    
    # Load report template
    if os.path.exists(report_template_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location("report_template", report_template_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        report_template_dict = module.report_template_dict
        print(f"Loaded category-specific report template from: {report_template_path}")
    else:
        from report_template import report_template_dict as default_report
        report_template_dict = default_report
        print(f"Using default report template (no category-specific template found)")
    
    # Load transcript template
    if os.path.exists(transcript_template_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location("transcript_template", transcript_template_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        transcript_template_dict = module.transcript_template_dict
        print(f"Loaded category-specific transcript template from: {transcript_template_path}")
    else:
        from transcript_template import transcript_template_dict as default_transcript
        transcript_template_dict = default_transcript
        print(f"Using default transcript template (no category-specific template found)")
    
    return report_template_dict, transcript_template_dict


# ============ Aspect Generation ============

def generate_balanced_aspect_sets(
    report_template_dict, 
    num_samples: int = 50
) -> List[tuple]:
    """
    Generate balanced sets of aspects with equal distribution across aspect counts (4-8).
    Returns list of (aspect_count, aspects_list) tuples.
    
    For 50 samples: 10 samples each for 4, 5, 6, 7, 8 aspects.
    """
    # Collect all aspects from the template
    all_aspects = []
    for key, value in report_template_dict.items():
        if isinstance(value, list):
            all_aspects.extend(value)
        else:
            all_aspects.append(value)
    
    all_aspects = list(set(all_aspects))  # Deduplicate
    
    # Define aspect counts to balance (4, 5, 6, 7, 8)
    aspect_counts = [4, 5, 6, 7, 8]
    samples_per_count = num_samples // len(aspect_counts)  # 10 for 50 samples
    remainder = num_samples % len(aspect_counts)
    
    all_sample_configs = []
    
    for i, aspect_num in enumerate(aspect_counts):
        # Distribute remainder across first few aspect counts
        count_for_this = samples_per_count + (1 if i < remainder else 0)
        
        for _ in range(count_for_this):
            # Sample aspects for this configuration
            if len(all_aspects) >= aspect_num:
                sampled = random.sample(all_aspects, aspect_num)
            else:
                sampled = all_aspects.copy()
            
            random.shuffle(sampled)
            all_sample_configs.append((aspect_num, sampled))
    
    # Shuffle the final list to mix different aspect counts
    random.shuffle(all_sample_configs)
    
    return all_sample_configs


# ============ LLM Generation Functions ============

def generate_detailed_aspect_descriptions(
    aspects: List[str], 
    category_name: str,
    model: str = "google/gemini-2.0-flash-001", 
    max_retries: int = 2, 
    temperature: float = 0.8
) -> Dict[str, str]:
    """Generate detailed descriptions for each aspect, tailored to the industry."""
    detailed_descriptions = {}
    for aspect in aspects:
        prompt = f"""You are a financial analyst specializing in the {category_name} industry.
Write a highly detailed and plausible explanation about the following financial aspect as if it were presented 
in an earnings call for a {category_name} company: "{aspect}". 

Include fictional but realistic figures, percentages, trends, technical initiatives, regional commentary, 
and strategic insights specific to the {category_name} industry. Be as specific as possible.
Use industry-appropriate terminology and reference realistic companies, products, or market conditions."""
        
        response = _chat_completion(prompt=prompt, model=model, max_retries=max_retries, temperature=temperature)
        detailed_descriptions[aspect] = response
    return detailed_descriptions


def generate_transcript_from_aspects_llm(
    template: str,
    aspects: List[str],
    aspect_descriptions: Dict[str, str],
    category_name: str,
    model: str = "google/gemini-2.0-flash-001",
    temperature: float = 0.7,
    max_retries: int = 2
) -> str:
    """Generate a full earnings call transcript from aspects and template."""
    
    prompt = f"""
You are a financial content writer tasked with generating a realistic, synthetic earnings call transcript 
for a {category_name} company that is approximately 3000 to 5000 words.

You will receive:
- A structured **template** outlining the order and roles of speakers (e.g., CEO, CFO, CTO).
- A list of **financial aspects** to be covered.
- A dictionary of **Aspect Descriptions**, which includes detailed narrative content for each aspect.

Your task is to fully incorporate all content from the Aspect Descriptions dictionary:
- Write a transcript that sounds like an actual {category_name} company earnings call.
- Follow the general structure of the template but feel natural and dynamic.
- **Every description in the Aspect Descriptions dictionary must be completely integrated into the transcript.**
- Do **not** include bullet points, section titles, or formatting indicators. Write as pure, flowing dialogue.
- Ensure that **all** entries from the Aspect Descriptions dictionary are **fully represented and paraphrased**.
- Use corporate and executive tone with {category_name} industry-specific terminology.
- Avoid repetition of phrasing between speakers. Ensure smooth transitions.
- Template placeholders may be assigned reasonable fictional values appropriate for {category_name} companies.

Return only the full transcript in plain text.

---
**Earnings Call Template (structure only):**
{template}

---
**Aspects to Cover:**
{json.dumps(aspects, indent=2)}

---
**Aspect Descriptions (content to integrate):**
{json.dumps(aspect_descriptions, indent=2)}

---
Before finalizing, review your output and ensure each aspect description is clearly and fully represented.
Now, generate the full transcript accordingly:
"""

    return _chat_completion(prompt=prompt, model=model, max_retries=max_retries, temperature=temperature)


def generate_aspect_summaries_from_transcript(
    aspects: List[str],
    transcript: str,
    model: str = "google/gemini-2.0-flash-001",
    max_retries: int = 2,
    temperature: float = 0.7
) -> Dict[str, str]:
    """Generate summaries for each aspect from the transcript using structured output."""
    
    aspects_str = "\n".join([f"- {a}" for a in aspects])
    
    prompt = f"""You will receive an earnings call transcript delimited by <article></article>. 
For each aspect listed below, write a concise summary that accurately captures what the transcript says about that aspect.

You MUST provide a summary for EVERY aspect listed below.

Aspects:
{aspects_str}

<article>
{transcript}
</article>"""

    try:
        # Try structured output first
        result = _chat_completion_structured(
            prompt=prompt,
            model=model,
            response_model=AspectSummary,
            max_retries=max_retries,
            temperature=temperature
        )
        if result:
            return result.summaries
    except Exception as e:
        print(f"Structured output failed, falling back to text parsing: {e}")
    
    # Fallback to text-based parsing
    fallback_prompt = prompt + """

Return your answer as pure JSON (no markdown, no extra text) in the form:
{
  "aspect name": "summary...",
  "aspect name": "summary...",
  ...
}"""
    
    summary_json_str = _chat_completion(fallback_prompt, model, max_retries, temperature)
    summary_json_str = summary_json_str.replace("```json", "").replace("```", "").strip()

    try:
        aspect_summary = json.loads(summary_json_str)
        return aspect_summary
    except json.JSONDecodeError:
        print(f"Failed to parse JSON response. Response was:\n{summary_json_str[:500]}...")
        return None


# ============ Main Entry Point ============

def main():
    parser = argparse.ArgumentParser(
        description="Generate synthetic earnings call data for multiple industry categories."
    )
    parser.add_argument(
        "--category", 
        type=str, 
        required=True,
        help="Category key to generate data for (e.g., software_saas, oil_gas)"
    )
    parser.add_argument(
        "--num_sample", 
        type=int, 
        default=50,
        help="Number of samples to generate (default: 50). Will be distributed equally across aspect counts 4-8."
    )
    parser.add_argument(
        "--model", 
        type=str, 
        default="google/gemini-2.0-flash-001",
        help="LLM model to use (default: google/gemini-2.0-flash-001 via OpenRouter)"
    )
    parser.add_argument(
        "--templates_dir", 
        type=str, 
        default="industry_templates",
        help="Directory containing industry-specific templates (default: industry_templates)"
    )
    parser.add_argument(
        "--output_dir", 
        type=str, 
        default="output",
        help="Output directory for generated data (default: output)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between samples in seconds (default: 1.0)"
    )
    
    args = parser.parse_args()
    
    # Load category info
    try:
        from company_categories import get_category_by_key
        category_config = get_category_by_key(args.category)
        if not category_config:
            print(f"Error: Category '{args.category}' not found.")
            from company_categories import get_category_keys
            print(f"Available categories: {', '.join(get_category_keys())}")
            return
        category_name = category_config['name']
    except ImportError:
        print("Warning: company_categories.py not found. Using category key as name.")
        category_name = args.category.replace("_", " ").title()
    
    print(f"\n{'='*60}")
    print(f"Generating synthetic data for: {category_name}")
    print(f"Category key: {args.category}")
    print(f"Model: {args.model}")
    print(f"Total samples: {args.num_sample}")
    print(f"Distribution: Equal across aspect counts 4, 5, 6, 7, 8")
    print(f"{'='*60}\n")
    
    # Load templates
    report_template_dict, transcript_template_dict = load_category_templates(
        args.category, 
        args.templates_dir
    )
    
    # Create output directory (organized by category only, aspect count in filename)
    output_folder = os.path.join(args.output_dir, args.category)
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder: {output_folder}")
    
    # Generate balanced aspect sets
    sample_configs = generate_balanced_aspect_sets(
        report_template_dict, 
        num_samples=args.num_sample
    )
    
    # Print distribution
    aspect_distribution = {}
    for aspect_num, _ in sample_configs:
        aspect_distribution[aspect_num] = aspect_distribution.get(aspect_num, 0) + 1
    print(f"Aspect distribution: {dict(sorted(aspect_distribution.items()))}")
    
    success_count = 0
    
    for i, (aspect_num, aspects) in enumerate(tqdm(sample_configs, desc=f"Generating {category_name} samples")):
        sample_index = i + 1
        # Include aspect count in filename for easy identification
        output_path = os.path.join(output_folder, f"sample_{sample_index:03d}_{aspect_num}aspects.json")
        
        # Skip if already exists
        if os.path.exists(output_path):
            print(f"Skipping existing: {output_path}")
            success_count += 1
            continue
        
        try:
            # Generate detailed descriptions
            aspect_descriptions = generate_detailed_aspect_descriptions(
                aspects, 
                category_name,
                model=args.model, 
                max_retries=2, 
                temperature=0.7
            )
            
            # Get template for this number of aspects
            template_key = str(aspect_num)
            template = transcript_template_dict.get(template_key)
            if not template:
                # Fall back to closest available template
                available_keys = sorted(transcript_template_dict.keys(), key=int)
                template_key = min(available_keys, key=lambda x: abs(int(x) - aspect_num))
                template = transcript_template_dict[template_key]
            
            # Generate transcript
            transcript = generate_transcript_from_aspects_llm(
                template=template,
                aspects=aspects,
                aspect_descriptions=aspect_descriptions,
                category_name=category_name,
                model=args.model,
                temperature=0.7,
                max_retries=2
            )
            
            # Generate summaries using structured output
            aspect_summary = generate_aspect_summaries_from_transcript(
                aspects=aspects,
                transcript=transcript,
                model=args.model,
                max_retries=2,
                temperature=0.7
            )
            
            if aspect_summary is None:
                print(f"Failed to generate summary for sample {sample_index}")
                continue
            
            # Save result
            result = {
                "document": transcript,
                "aspects": aspects,
                "aspect_summary": aspect_summary,
                "num_aspects": aspect_num,
                "category": args.category,
                "category_name": category_name
            }
            
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            success_count += 1
            
            # Delay between samples
            if i < len(sample_configs) - 1:
                time.sleep(args.delay)
                
        except Exception as e:
            print(f"Error generating sample {sample_index}: {e}")
            continue
    
    print(f"\n{'='*60}")
    print(f"Completed: {success_count}/{args.num_sample} samples generated successfully")
    print(f"Output saved to: {output_folder}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
