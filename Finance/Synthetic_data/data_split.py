"""
Data Split Script for Multi-Category Synthetic Data

Splits the generated synthetic earnings call data into train and test sets,
maintaining balanced distribution across categories and aspect counts.
"""

import os
import json
import random
from collections import defaultdict
from sklearn.model_selection import train_test_split

# Configuration
OUTPUT_DIR = './output'
TRAIN_RATIO = 0.8  # 80% train, 20% test
RANDOM_SEED = 42

def collect_all_samples(output_dir):
    """Collect all JSON sample files from the output directory."""
    samples = []
    
    for category in os.listdir(output_dir):
        category_path = os.path.join(output_dir, category)
        if not os.path.isdir(category_path):
            continue
            
        for filename in os.listdir(category_path):
            if not filename.endswith('.json'):
                continue
                
            file_path = os.path.join(category_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Extract metadata
                num_aspects = data.get('num_aspects', len(data.get('aspects', [])))
                category_name = data.get('category', category)
                
                samples.append({
                    'path': file_path,
                    'category': category_name,
                    'num_aspects': num_aspects,
                    'data': data
                })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
    
    return samples


def stratified_split(samples, train_ratio=0.8, seed=42):
    """
    Perform stratified split by category and aspect count.
    Ensures balanced distribution in both train and test sets.
    """
    random.seed(seed)
    
    # Group samples by (category, num_aspects)
    groups = defaultdict(list)
    for sample in samples:
        key = (sample['category'], sample['num_aspects'])
        groups[key].append(sample)
    
    train_samples = []
    test_samples = []
    
    # Split each group
    for key, group_samples in groups.items():
        if len(group_samples) == 1:
            # If only one sample, add to train
            train_samples.extend(group_samples)
        else:
            # Stratified split within the group
            n_train = max(1, int(len(group_samples) * train_ratio))
            random.shuffle(group_samples)
            train_samples.extend(group_samples[:n_train])
            test_samples.extend(group_samples[n_train:])
    
    return train_samples, test_samples


def validate_samples(samples):
    """Validate sample quality - filter out problematic samples."""
    valid_samples = []
    
    for sample in samples:
        data = sample['data']
        
        # Check for empty document
        document = data.get('document', '').strip()
        if not document:
            print(f"Skipping {sample['path']}: Empty document")
            continue
        
        # Check for problematic summaries
        aspect_summary = data.get('aspect_summary', {})
        has_issue = False
        for summary in aspect_summary.values():
            if isinstance(summary, str) and "does not" in summary.lower():
                has_issue = True
                break
        
        if has_issue:
            print(f"Skipping {sample['path']}: Problematic summary")
            continue
        
        valid_samples.append(sample)
    
    return valid_samples


def save_split(train_samples, test_samples, output_prefix=''):
    """Save train and test splits as JSON files."""
    
    # Save paths only (for compatibility with existing code)
    train_paths = [s['path'] for s in train_samples]
    test_paths = [s['path'] for s in test_samples]
    
    train_file = f'{output_prefix}train.json' if output_prefix else 'train.json'
    test_file = f'{output_prefix}test.json' if output_prefix else 'test.json'
    
    with open(train_file, 'w', encoding='utf-8') as f:
        json.dump(train_paths, f, indent=2, ensure_ascii=False)
    
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(test_paths, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved {train_file}: {len(train_paths)} samples")
    print(f"✅ Saved {test_file}: {len(test_paths)} samples")
    
    return train_paths, test_paths


def print_statistics(samples, label=""):
    """Print distribution statistics for a set of samples."""
    
    # By category
    category_counts = defaultdict(int)
    for s in samples:
        category_counts[s['category']] += 1
    
    # By aspect count
    aspect_counts = defaultdict(int)
    for s in samples:
        aspect_counts[s['num_aspects']] += 1
    
    print(f"\n{'='*50}")
    print(f"{label} Statistics ({len(samples)} total samples)")
    print(f"{'='*50}")
    
    print("\nBy Category:")
    for cat in sorted(category_counts.keys()):
        print(f"  {cat}: {category_counts[cat]}")
    
    print("\nBy Aspect Count:")
    for num in sorted(aspect_counts.keys()):
        print(f"  {num} aspects: {aspect_counts[num]}")


def main():
    print("=" * 60)
    print("Multi-Category Data Split")
    print("=" * 60)
    
    # Step 1: Collect all samples
    print(f"\n📂 Collecting samples from: {OUTPUT_DIR}")
    all_samples = collect_all_samples(OUTPUT_DIR)
    print(f"   Found {len(all_samples)} total samples")
    
    # Step 2: Validate samples
    print("\n🔍 Validating samples...")
    valid_samples = validate_samples(all_samples)
    print(f"   {len(valid_samples)} valid samples after filtering")
    
    # Step 3: Print overall statistics
    print_statistics(valid_samples, "Overall")
    
    # Step 4: Perform stratified split
    print(f"\n✂️ Performing stratified split (train={TRAIN_RATIO*100:.0f}%, test={100-TRAIN_RATIO*100:.0f}%)...")
    train_samples, test_samples = stratified_split(valid_samples, TRAIN_RATIO, RANDOM_SEED)
    
    # Step 5: Print split statistics
    print_statistics(train_samples, "Train Set")
    print_statistics(test_samples, "Test Set")
    
    # Step 6: Save splits
    print("\n💾 Saving split files...")
    save_split(train_samples, test_samples)
    
    print("\n✅ Data split complete!")


if __name__ == "__main__":
    main()
