import os
import json
from sklearn.model_selection import train_test_split

filtered_path = 'gemini_filtered_data'
flash_path = 'gemini-2.0-flash'

test_paths = []
for root, dirs, files in os.walk(filtered_path):
    for file in files:
        if file.endswith('.json'):
            test_paths.append(os.path.join(root, file))


filtered_ids = {os.path.basename(p) for p in test_paths}
train_candidates = []

for root, dirs, files in os.walk(flash_path):
    for filename in files:
        if not filename.endswith('.json') or filename in filtered_ids:
            continue

        file_path = os.path.join(root, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            continue  


        aspect_summary = data.get("aspect_summary", {})
        if any("does not" in summary.lower() for summary in aspect_summary.values()):
            continue

        content_key = "document"  
        content = data.get(content_key, '').strip()
        if content:
            train_candidates.append(file_path)



with open('train.json', 'w', encoding='utf-8') as f:
    json.dump(train_candidates, f, indent=2, ensure_ascii=False)


with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(test_paths, f, indent=2, ensure_ascii=False)

