"""
Generate Industry-Specific Templates for Multi-Category Synthetic Data Generation

This script uses LLMs to generate report templates and transcript templates
for each company category defined in company_categories.py.
"""

import os
import json
import time
import argparse
from typing import Dict
import openai

from dotenv import load_dotenv
from company_categories import COMPANY_CATEGORIES, get_category_keys, get_category_by_key

load_dotenv()


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


def generate_report_template(category_key: str, category_config: Dict, model: str) -> str:
    """Generate a report template for a specific industry category."""
    
    prompt = f"""You are a financial analyst expert. Generate a Python dictionary that defines the key financial aspects 
for earnings call reports in the {category_config['name']} industry ({category_config['sector']} sector).

The output should be a Python file with an OrderedDict called `report_template_dict`.
Each key in the dictionary should be a major category of financial discussion, 
and each value should be a list of specific aspects to cover under that category.

Use the following industry context:
- Industry: {category_config['name']}
- Sector: {category_config['sector']}
- Key Metrics: {', '.join(category_config['key_metrics'])}

Base the aspects on these industry-specific topics: 
{json.dumps(category_config['aspects'], indent=2)}

Generate a structured report template with 6-8 major categories, each containing 1-4 specific aspects.
The aspects should be specific, measurable, and relevant to {category_config['name']} company earnings calls.

Return ONLY valid Python code with no markdown formatting. The code should start with:
from collections import OrderedDict

report_template_dict = OrderedDict([
    ...
])

Make sure to properly escape any quotes within strings."""

    return _chat_completion(prompt, model, temperature=0.7)


def generate_transcript_template(category_key: str, category_config: Dict, model: str) -> str:
    """Generate transcript templates for a specific industry category."""
    
    executive_roles = category_config['executive_roles']
    
    prompt = f"""You are an expert in corporate communications. Generate Python code containing earnings call transcript templates
for the {category_config['name']} industry ({category_config['sector']} sector).

The output should be a Python file with an OrderedDict called `transcript_template_dict`.
Keys should be strings "4", "5", "6", "7", "8" representing the number of aspects to cover.
Values should be multi-line string templates for earnings call transcripts.

Key requirements:
1. Industry: {category_config['name']} ({category_config['sector']} sector)
2. Executive roles to include: {', '.join(executive_roles)}
3. Templates should include placeholders like:
   - {{company_name}}, {{quarter}}, {{ir_name}}, {{ir_title}}
   - {{ceo_name}}, {{cfo_name}}, and other role-specific names
   - {{aspect_1_details}}, {{aspect_2_details}}, etc. for content placeholders
   - {{new_product}}, {{impact_of_product}} for industry-specific elements

4. Structure each template with:
   - Operator introduction
   - IR representative introduction  
   - CEO opening remarks
   - CFO financial discussion
   - Other executives (based on industry) for operational/technical updates
   - Q&A session with 2-4 analyst questions
   - Closing remarks

5. For template "4", include placeholders for 4 aspects (aspect_1 through aspect_4)
   For template "5", include 5 aspects, and so on up to template "8"

6. Make the templates realistic for {category_config['name']} earnings calls, 
   using industry-appropriate terminology and discussion topics.

Return ONLY valid Python code with no markdown formatting. The code should start with:
from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", \"\"\"
    ...
    \"\"\"),
    ...
])

Ensure all quotes within template strings are properly escaped or use matching quote styles."""

    return _chat_completion(prompt, model, temperature=0.7)


def save_template(content: str, output_path: str, dry_run: bool = False):
    """Save generated template to file."""
    if dry_run:
        print(f"\n{'='*60}")
        print(f"DRY RUN - Would save to: {output_path}")
        print(f"{'='*60}")
        print(content[:2000] + "..." if len(content) > 2000 else content)
        return
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved: {output_path}")


def clean_python_code(code: str) -> str:
    """Remove markdown code blocks if present."""
    code = code.strip()
    if code.startswith("```python"):
        code = code[9:]
    elif code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]
    return code.strip()


def generate_templates_for_category(
    category_key: str, 
    model: str, 
    output_dir: str,
    dry_run: bool = False,
    skip_report: bool = False,
    skip_transcript: bool = False
):
    """Generate both report and transcript templates for a category."""
    
    category_config = get_category_by_key(category_key)
    if not category_config:
        print(f"Error: Category '{category_key}' not found.")
        return False
    
    category_output_dir = os.path.join(output_dir, category_key)
    
    print(f"\n{'='*60}")
    print(f"Generating templates for: {category_config['name']} ({category_key})")
    print(f"{'='*60}")
    
    # Generate report template
    if not skip_report:
        print(f"Generating report template...")
        report_content = generate_report_template(category_key, category_config, model)
        report_content = clean_python_code(report_content)
        report_path = os.path.join(category_output_dir, "report_template.py")
        save_template(report_content, report_path, dry_run)
    
    # Generate transcript template
    if not skip_transcript:
        print(f"Generating transcript template...")
        transcript_content = generate_transcript_template(category_key, category_config, model)
        transcript_content = clean_python_code(transcript_content)
        transcript_path = os.path.join(category_output_dir, "transcript_template.py")
        save_template(transcript_content, transcript_path, dry_run)
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate industry-specific report and transcript templates using LLMs."
    )
    parser.add_argument(
        "--category", 
        type=str, 
        default=None,
        help=f"Category key to generate templates for. Available: {', '.join(get_category_keys())}"
    )
    parser.add_argument(
        "--all", 
        action="store_true",
        help="Generate templates for all categories"
    )
    parser.add_argument(
        "--model", 
        type=str, 
        default="google/gemini-2.0-flash-001",
        help="LLM model to use for generation (default: google/gemini-2.0-flash-001 via OpenRouter)"
    )
    parser.add_argument(
        "--output-dir", 
        type=str, 
        default="industry_templates",
        help="Output directory for generated templates (default: industry_templates)"
    )
    parser.add_argument(
        "--dry-run", 
        action="store_true",
        help="Print generated content without saving to files"
    )
    parser.add_argument(
        "--skip-report",
        action="store_true",
        help="Skip generating report templates"
    )
    parser.add_argument(
        "--skip-transcript",
        action="store_true",
        help="Skip generating transcript templates"
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=2,
        help="Delay in seconds between API calls (default: 2)"
    )
    
    args = parser.parse_args()
    
    if not args.category and not args.all:
        print("Error: Please specify --category <key> or --all")
        print(f"Available categories: {', '.join(get_category_keys())}")
        return
    
    categories_to_process = get_category_keys() if args.all else [args.category]
    
    print(f"Model: {args.model}")
    print(f"Output directory: {args.output_dir}")
    print(f"Categories to process: {len(categories_to_process)}")
    if args.dry_run:
        print("DRY RUN MODE - No files will be saved")
    
    success_count = 0
    for i, category_key in enumerate(categories_to_process):
        try:
            success = generate_templates_for_category(
                category_key=category_key,
                model=args.model,
                output_dir=args.output_dir,
                dry_run=args.dry_run,
                skip_report=args.skip_report,
                skip_transcript=args.skip_transcript
            )
            if success:
                success_count += 1
            
            # Add delay between categories to avoid rate limiting
            if i < len(categories_to_process) - 1:
                time.sleep(args.delay)
                
        except Exception as e:
            print(f"Error processing category '{category_key}': {e}")
    
    print(f"\n{'='*60}")
    print(f"Completed: {success_count}/{len(categories_to_process)} categories processed successfully")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
