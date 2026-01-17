import os
import json
from sklearn.model_selection import train_test_split

# 資料夾路徑
filtered_path = './gemini_filtered_data'
flash_path = './gemini-2.0-flash'

# Step 1: 收集 test.json 檔案路徑（來自 gemini_filtered_data）
test_paths = []
for root, dirs, files in os.walk(filtered_path):
    for file in files:
        if file.endswith('.json'):
            test_paths.append(os.path.join(root, file))

print(f"✅ 已收集 {len(test_paths)} 個 test.json 檔案路徑")

# Step 2: 過濾 gemini-2.0-flash
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
            continue  # 跳過 JSON 解析錯誤的檔案

        # 篩選邏輯
        aspect_summary = data.get("aspect_summary", {})
        if any("does not" in summary.lower() for summary in aspect_summary.values()):
            continue

        content_key = "document"  # 根據實際欄位名稱可修改
        content = data.get(content_key, '').strip()
        if content:
            train_candidates.append(file_path)



# Step 4: 寫入 json 檔案
with open('train.json', 'w', encoding='utf-8') as f:
    json.dump(train_candidates, f, indent=2, ensure_ascii=False)

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(test_paths, f, indent=2, ensure_ascii=False)

print("✅ 已完成 train.json, valid.json, test.json 的產生")
