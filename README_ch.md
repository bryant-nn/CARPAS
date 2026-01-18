# CARPAS- Towards Content-Aware Refinement of Provided Aspects for Summarization in Large Language Models

專案涵蓋：
- ✅ **Synthetic Data 產生**
- ✅ **Direct / Chain-of-Thought / Self-Consistency Prompt**
- ✅ **LangGraph multi-step reasoning (Agentic)**
- ✅ **多維度自動評估（LLM + BERTScore）**

---

## 📦 專案總覽

```

.
├── Finance/
├── Covid/
├── Real_word_data/
├── requirements.txt
└── README.md

```

### 📁 資料集（Datasets）

本專案包含三個資料集：

| Dataset | 說明 |
|------|------|
| `Finance/` | 合成財報 / earnings call 類型文件 |
| `Covid/` | 疫情 / 公共衛生報告 |
| `Real_word_data/` | 真實世界文件|

每個資料集結構完全一致，方便跨資料集比較。

---

## 📂 Dataset 結構說明（共通）

```

Dataset/
├── Method/           # LLM 推理與摘要方法
├── Result/           # 模型輸出與評估結果
└── Synthetic_data/   # 合成資料產生與切分

````

---

## 🧬 Synthetic_data — 合成資料產生

### 🎯 功能
使用 LLM（Gemini / GPT）產生 **可控 aspect 結構的長文件**，作為實驗資料來源。

### 🔑 核心檔案

| 檔案 | 功能 |
|----|----|
| `data_generation_gemini.py` | 使用 Gemini 產生合成文件與 aspect summaries |
| `report_template.py` | aspect pool 與主題模板 |
| `transcript_template.py` | 文件結構模板（如 earnings call） |
| `data_split.py` | 切分 train / test |
| `train.json` | 訓練資料路徑清單 |
| `test.json` | 測試資料路徑清單 |

### ▶️ 產生合成資料
生成20份文件，每份包含4個aspect： 
```bash
cd Finance/Synthetic_data
python data_generation_gemini.py \
  --num_sample 20 \
  --num_aspect 4
```

輸出格式（每個 `.json`）：

```json
{
  "document": "... long document ...",
  "aspects": ["Aspect A", "Aspect B"],
  "aspect_summary": {
    "Aspect A": "summary...",
    "Aspect B": "summary..."
  }
}
```

這些檔案會依模型與 aspect 數量存放，例如：

```
Synthetic_data/
└── gemini-2.0-flash/
    └── 4/
        ├── sample_1.json
        ├── sample_2.json
        └── ...
```

### 合成資料品質過濾與切分（Data Filtering & Split）

由於 synthetic data 可能包含：

- 不完整文件

- aspect summary 出現否定 / 無效描述

- 文件內容為空或品質過低

因此在正式實驗前，必須進行資料過濾與切分。

🔑 核心檔案
| 檔案 | 功能 |
|----|----|
data_split.py	| 過濾低品質資料，並產生 train.json / test.json


## 🧠 data_split.py 過濾邏輯說明

`data_split.py` 會執行以下資料過濾與切分流程：

### ① 收集已通過篩選的 test 資料
- 從 `gemini_filtered_data/` 目錄中蒐集所有 `.json` 檔案
- 作為固定的測試資料來源（test set）

### ② 過濾原始 synthetic data
以下情況的資料會被排除：
- aspect summary 中包含否定語句（如 `"does not"`）
- 文件內容為空
- JSON 檔案無法正確解析

### ③ 避免資料重複
- 確保 `train` 資料與 `test` 資料 **不重疊**
- 避免資料洩漏（data leakage），確保實驗公平性

### ④ 輸出資料清單
- `train.json`：過濾後的高品質訓練 / warm-up 資料路徑清單  
- `test.json`：固定測試資料，用於後續 Prompt / LangGraph 評估

---

## ▶️ 執行資料過濾與切分

```bash
cd Finance/Synthetic_data
python data_split.py
```

---

## 🧠 Method — Aspect Summarization

### 兩種主要方法

| 方法           | 檔案                    | 特點                          |
| ------------ | --------------------- | --------------------------- |
| Prompt-based | `prompt.py`           | Direct / CoT / CoT Self-Consistency |
| Agentic-based  | `langgraph_guided.py` | Self-Refine Prompt             |

---

## 🧩 prompt.py — Prompt-based 方法

### 🔹 支援模式

| `cot_mode` | 說明                        |
| ---------- | ------------------------- |
| `direct`   | 無推理，直接輸出                  |
| `cot`      | Chain-of-Thought          |
| `cot_sc`   | Self-Consistency（多次取樣再整合） |

### 🔹 y / n 參數說明

| 參數  | 意義                               |
| --- | -------------------------------- |
| `y` | 從 ground truth 中抽樣的正確 aspects 數量 |
| `n` | 隨機加入的不相關 aspects 數量              |

→ 用來測試模型 **過濾錯誤主題與補齊缺失主題的能力**

### ▶️ 執行範例
- 執行 Preliminary with Direct Prompt
```bash
cd Covid/Method

python prompt.py \
  --cot_mode direct \
  --model gpt-4o \
  --y 2 \
  --n 2 \
```

- 輸出位置

```
Result/
└── cot_sc_prompt_with_predicted_aspect/
    └── gemini_filtered_data_y2n2/
        └── gpt-4o/
            └── 4_sample_12.json
```
  
- 執行 #Aspect-LLM with CoT-SC
```bash
cd Covid/Method

python prompt.py \
  --cot_mode cot_sc \
  --model gemini-2.5-flash-lite \
  --y 2 \
  --n 2 \
  --gemini_api_key YOUR_GEMINI_API_KEY \
  --provide_aspect_num \
  --aspect_source predict
```
- 輸出位置
```
Result/
└── cot_sc_prompt_with_predicted_aspect/
    └── gemini_filtered_data_y2n2/
        └── gemini-2.5-flash-lite/
            └── 4_sample_12.json
```

- 執行 #Aspect-RM with CoT
```bash
cd Covid/Method

python prompt.py \
  --cot_mode cot \
  --model gemma-3-12b \
  --y 2 \
  --n 2 \
  --gemini_api_key YOUR_GEMINI_API_KEY \
  --provide_aspect_num \
  --aspect_source csv
```
- 輸出位置
```Result/
└── cot_prompt_with_csv_aspect/
    └── gemini_filtered_data_y2n2/
        └── gemma-3-12b/
            └── 4_sample_12.json
```

---

## 🔗 langgraph_guided.py — Self-Refine Prompt

### 🔹 流程概念

1. **Check coverage**：判斷目前 aspects 是否已涵蓋文章重點
2. **Revise aspects**：保留 / 修改 / 刪除 / 新增 aspects
3. **Iterate**（最多 ~14 步）
4. **Summarize aspects**

### ▶️ 執行範例
- 執行 Preliminary
```bash
cd Covid/Method

python langgraph_guided.py \
  --model gpt-4o-mini \
  --memory False \
  --y 2 \
  --n 2 \
  --api_key YOUR_OPENAI_API_KEY
```
- 輸出位置
```
Result/
└── langgraph/no_memory/
    └── gemini_filtered_data_y2n2/
        └── gpt-4o-mini/
            └── 4_sample_12.json
```
- 執行 #Aspect-LLM
```bash
cd Covid/Method

python langgraph_guided.py \
  --model gpt-4o-mini \
  --memory False \
  --y 2 \
  --n 2 \
  --provide_aspect_num \
  --aspect_source predict \
  --api_key YOUR_OPENAI_API_KEY
```
- 輸出位置
```
Result/
└── langgraph_prompt_with_predicted_aspect/no_memory/
    └── gemini_filtered_data_y2n2/
        └── gpt-4o-mini/
            └── 4_sample_12.json
```
- 執行 #Aspect-RM
```bash
cd Covid/Method

python langgraph_guided.py \
  --model gpt-4o-mini \
  --memory False \
  --y 2 \
  --n 2 \
  --provide_aspect_num \
  --aspect_source csv \
  --api_key YOUR_OPENAI_API_KEY
```
- 輸出位置
```
Result/
└── langgraph_prompt_with_csv_aspect/no_memory/
    └── gemini_filtered_data_y2n2/
        └── gpt-4o-mini/
            └── 4_sample_12.json
```

---

## 📊 Result — 模型輸出結果

每個輸出 `.json` 內容包含：

```json
{
  "document": "...",
  "ground_truth_aspects": [...],
  "ground_truth_aspect_summary": {...},
  "provided_aspects": [...],
  "generated_revised_aspects_summary": {...},
  "pairing": {...},
  "metrics": {...},
  "total_steps": 4,
  "total_tokens": 12021,
  "predicted_aspect_num": 2
}
```

## 📏 Chat Evaluation — 自動評估

### 🔍 評估指標

| 指標               | 說明                      |
| ---------------- | ----------------------- |
| Factuality       | LLM 判斷摘要是否忠於原文          |
| Relevance        | aspect coverage + 數量合理性 |
| Aspect BERTScore | aspect 名稱語意對齊程度         |

### ▶️ 執行評估

```bash
cd Covid/Method
python chat_eval.py
```

輸出會寫入：

```
Result/Chat_eval/...
```

---

## ⚙️ 環境設定

```bash
pip install -r requirements.txt
```

`.env` 需包含（視使用模型）：

```env
OPENAI_API_KEY=...
GEMINI_API_KEY=...
```

---

## 🔁 建議實驗流程（Quick Start）

```text
1. Synthetic_data/
   ├── data_generation_gemini.py
   └── data_split.py

2. Method/
   ├── prompt.py
   └── langgraph_guided.py

3. Method/
   └── chat_eval.py
```

## 🔢 train_ddp.py — Aspect 數量預測模型（DDP 訓練）

`train_ddp.py` 用於訓練一個 **文件層級的 Aspect 數量預測模型**，目標是根據整篇文章內容，自動預測該文件中應該包含的 **aspect 數量**。

此模型的預測結果可用於：
- 在 `prompt.py` / `langgraph_guided.py` 中作為 **aspect 數量提示（count hint）**
- 協助 LLM 生成「數量合理、不過多也不過少」的 aspects
- 降低 hallucination 與過度切分主題的問題

---

### 🧠 模型概念

- **任務類型**：回歸（Regression）
- **輸入**：完整文章（document）
- **輸出**：該文章的 aspect 數量（整數）
- **Loss**：L1 Loss（MAE）
- **評估指標**：
  - MAE（Mean Absolute Error）
  - Rounded Accuracy（四捨五入後是否預測正確）

---

### 🏗 模型架構

- **Base Model**：`Qwen/Qwen3-Embedding-0.6B`
- **Pooling**：Mean Pooling over token embeddings
- **Head**：MLP Regression Head
- **Fine-tuning 方法**：
  - LoRA（PEFT）
  - 僅微調 attention / MLP 子模組
- **訓練方式**：
  - 支援單卡 / 多卡 Distributed Data Parallel (DDP)

---

### 📂 訓練資料來源

- 由 `Synthetic_data/data_split.py` 產生：
  - `train.json`
  - `test.json`
- 每筆資料包含：
  - `document`
  - `aspects`（用於計算 ground-truth aspect 數量）

---

### ▶️ 訓練模型

```bash
cd Covid/Method

python train_ddp.py \
  --mode train \
  --output_dir aspect_count_model
