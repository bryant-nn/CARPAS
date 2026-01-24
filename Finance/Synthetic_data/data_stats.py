"""
Data Statistics Script for Multi-Category Synthetic Data

Analyzes the generated synthetic earnings call data and produces statistics
grouped by category and aspect count.
"""

import os
import json
import pandas as pd
import tiktoken
from collections import defaultdict

# Initialize GPT tokenizer
tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")

def count_tokens(text: str) -> int:
    """Count tokens in text using tiktoken."""
    return len(tokenizer.encode(text))


def collect_samples_from_output(output_dir='./output'):
    """Collect all sample file paths from the output directory."""
    samples = []
    
    for category in os.listdir(output_dir):
        category_path = os.path.join(output_dir, category)
        if not os.path.isdir(category_path):
            continue
            
        for filename in os.listdir(category_path):
            if filename.endswith('.json'):
                samples.append(os.path.join(category_path, filename))
    
    return samples


def analyze_by_category(file_paths):
    """Analyze samples grouped by category."""
    category_stats = defaultdict(lambda: {
        "total_files": 0,
        "total_aspects": 0,
        "total_summary_tokens": 0,
        "total_doc_tokens": 0,
        "aspect_counts": defaultdict(int),
    })
    
    for path in file_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {path}: {e}")
            continue
        
        category = data.get("category", "unknown")
        num_aspects = data.get("num_aspects", len(data.get("aspects", [])))
        document = data.get("document", "")
        aspect_summary = data.get("aspect_summary", {})
        
        stats = category_stats[category]
        stats["total_files"] += 1
        stats["total_aspects"] += num_aspects
        stats["total_doc_tokens"] += count_tokens(document)
        stats["aspect_counts"][num_aspects] += 1
        
        for summary in aspect_summary.values():
            if isinstance(summary, str):
                stats["total_summary_tokens"] += count_tokens(summary)
    
    # Build DataFrame
    rows = []
    for category, stats in sorted(category_stats.items()):
        total_files = stats["total_files"]
        rows.append({
            "category": category,
            "total_files": total_files,
            "total_aspects": stats["total_aspects"],
            "avg_doc_tokens": round(stats["total_doc_tokens"] / total_files, 2) if total_files else 0,
            "avg_summary_tokens": round(stats["total_summary_tokens"] / stats["total_aspects"], 2) if stats["total_aspects"] else 0,
            "aspect_distribution": dict(stats["aspect_counts"]),
        })
    
    # Add totals row
    total_files = sum(s["total_files"] for s in category_stats.values())
    total_aspects = sum(s["total_aspects"] for s in category_stats.values())
    total_doc_tokens = sum(s["total_doc_tokens"] for s in category_stats.values())
    total_summary_tokens = sum(s["total_summary_tokens"] for s in category_stats.values())
    
    # Aggregate aspect_distribution across all categories
    total_aspect_distribution = defaultdict(int)
    for stats in category_stats.values():
        for num_aspects, count in stats["aspect_counts"].items():
            total_aspect_distribution[num_aspects] += count
    
    rows.append({
        "category": "TOTAL",
        "total_files": total_files,
        "total_aspects": total_aspects,
        "avg_doc_tokens": round(total_doc_tokens / total_files, 2) if total_files else 0,
        "avg_summary_tokens": round(total_summary_tokens / total_aspects, 2) if total_aspects else 0,
        "aspect_distribution": dict(sorted(total_aspect_distribution.items())),
    })
    
    return pd.DataFrame(rows)


def analyze_by_aspect_count(file_paths):
    """Analyze samples grouped by number of aspects."""
    aspect_stats = defaultdict(lambda: {
        "total_files": 0,
        "total_doc_tokens": 0,
        "total_summary_tokens": 0,
        "categories": defaultdict(int),
    })
    
    for path in file_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue
        
        category = data.get("category", "unknown")
        num_aspects = data.get("num_aspects", len(data.get("aspects", [])))
        document = data.get("document", "")
        aspect_summary = data.get("aspect_summary", {})
        
        stats = aspect_stats[num_aspects]
        stats["total_files"] += 1
        stats["total_doc_tokens"] += count_tokens(document)
        stats["categories"][category] += 1
        
        for summary in aspect_summary.values():
            if isinstance(summary, str):
                stats["total_summary_tokens"] += count_tokens(summary)
    
    # Build DataFrame
    rows = []
    for num_aspects, stats in sorted(aspect_stats.items()):
        total_files = stats["total_files"]
        rows.append({
            "num_aspects": num_aspects,
            "total_files": total_files,
            "avg_doc_tokens": round(stats["total_doc_tokens"] / total_files, 2) if total_files else 0,
            "avg_summary_tokens_per_aspect": round(stats["total_summary_tokens"] / (total_files * num_aspects), 2) if total_files else 0,
            "num_categories": len(stats["categories"]),
        })
    
    # Add totals
    total_files = sum(s["total_files"] for s in aspect_stats.values())
    total_doc_tokens = sum(s["total_doc_tokens"] for s in aspect_stats.values())
    total_summary_tokens = sum(s["total_summary_tokens"] for s in aspect_stats.values())
    total_aspects = sum(num * s["total_files"] for num, s in aspect_stats.items())
    
    rows.append({
        "num_aspects": "TOTAL",
        "total_files": total_files,
        "avg_doc_tokens": round(total_doc_tokens / total_files, 2) if total_files else 0,
        "avg_summary_tokens_per_aspect": round(total_summary_tokens / total_aspects, 2) if total_aspects else 0,
        "num_categories": 20,
    })
    
    return pd.DataFrame(rows)


def main():
    print("=" * 60)
    print("Multi-Category Data Statistics")
    print("=" * 60)
    
    # Collect samples
    output_dir = './output'
    print(f"\n📂 Collecting samples from: {output_dir}")
    file_paths = collect_samples_from_output(output_dir)
    print(f"   Found {len(file_paths)} samples")
    
    # Analyze by category
    print("\n📊 Analyzing by category...")
    df_category = analyze_by_category(file_paths)
    print(df_category.to_string(index=False))
    df_category.to_csv("stats_by_category.csv", index=False)
    print("   Saved: stats_by_category.csv")
    
    # Analyze by aspect count
    print("\n📊 Analyzing by aspect count...")
    df_aspect = analyze_by_aspect_count(file_paths)
    print(df_aspect.to_string(index=False))
    df_aspect.to_csv("stats_by_aspect_count.csv", index=False)
    print("   Saved: stats_by_aspect_count.csv")
    
    print("\n✅ Statistics analysis complete!")


if __name__ == "__main__":
    main()
