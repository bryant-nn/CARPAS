import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv
import torch 
from bert_score import BERTScorer 
from tqdm import tqdm

# 建議使用 .env 檔案來管理你的 API 金鑰
# pip install python-dotenv
load_dotenv()

# 初始化 OpenAI client
# 程式會自動從環境變數 OPENAI_API_KEY 讀取金鑰
try:
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key=os.getenv("QWEN_API_KEY2")
  )
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    print("Please make sure your OPENAI_API_KEY is set as an environment variable.")
    exit()

class ChatEval:
    """
    使用大型語言模型 (LLM) 來評估生成文本的品質。
    """
    def __init__(self, model_name='gpt-4-turbo-preview'):
        """
        初始化 ChatEval。
        Args:
            model_name (str): 要使用的 OpenAI 模型名稱。
        """
        self.model_name = model_name

    def _ask_gpt(self, prompt: str) -> str:
        """
        向 OpenAI API 發送請求並獲取回應。
        """
        try:
            completion = client.chat.completions.create(
                # model=self.model_name,
                model="qwen/qwen3-next-80b-a3b-instruct",
                messages=[
                    {"role": "system", "content": "You are a helpful epidemic data analyst assistant designed to provide ratings and justifications."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500,
                # stream=True
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"An error occurred while calling the OpenAI API: {e}")
            print(1/0)
            return "Error: Could not get a response from the model."

    def get_score_and_reason(self, prompt: str) -> (int, str):
        """
        從 LLM 的回應中解析出分數和理由。
        返回一個 (score, reason) 的元組。
        """
        response = self._ask_gpt(prompt)
        
        # 使用正則表達式尋找回應開頭的第一個 1-5 的數字
        score_match = re.match(r"\s*([1-5])", response)
        
        if score_match:
            score = int(score_match.group(1))
            # 理由是分數之後的所有內容
            reason = response[score_match.end():].strip().lstrip('.').strip()
            return score, reason
        else:
            print(f"=== Error: Could not parse score from response ===\nResponse: {response}\n")
            return 0, "Failed to parse score from response."

    def evaluate_factuality(self, document: str, generated_summary: str) -> (int, str):
        """
        評估生成摘要的真實性 (Factuality)。
        
        Args:
            document (str): 原始的來源文件。
            generated_summary (str): 由模型生成的摘要。

        Returns:
            (int, str): (分數, 理由)
        """
        prompt_template = """You are a meticulous public health expert. Your task is to evaluate the FACTUALITY of a given summary based on the original pandemic press briefing transcript.

        Instructions:
        1. Read the original transcript carefully.
        2. Read the generated summary.
        3. Compare the summary against the transcript. The summary must be fully supported by the information present in the transcript.
        4. Rate the factuality on a scale of 1 to 5.
        
        Scoring Criteria:
        - 5 (Excellent): The summary is completely accurate. All claims, figures, and statements in the summary are directly supported by the transcript. No hallucinations or contradictions.
        - 4 (Good): The summary is mostly accurate, but might contain very minor inaccuracies or slight misinterpretations that don't affect the overall meaning.
        - 3 (Fair): The summary contains some noticeable factual errors or information that cannot be verified from the transcript.
        - 2 (Poor): The summary contains significant factual errors or major hallucinations that are misleading.
        - 1 (Very Poor): The summary is almost entirely fabricated or contradicts the transcript.

        Original Transcript:
        ---
        {document}
        ---

        Generated Summary to Evaluate:
        ---
        {summary}
        ---
        
        Please provide your rating first, followed by a brief reason.
        
        Return Format: [Number]. [Reason]

        Example Response: 4. The summary is mostly accurate, but it incorrectly states that the vaccination rate for the 5-11 age group was 50%...
        """
        prompt = prompt_template.format(document=document, summary=generated_summary)
        return self.get_score_and_reason(prompt)

    def evaluate_relevance(self, ground_truth_aspects: list, generated_aspects: list) -> (int, str):
        """
        評估生成的主題 (aspects) 的相關性 (Relevance)，同時考慮主題數量。

        Args:
            ground_truth_aspects (list): 人工標註的黃金標準主題列表。
            generated_aspects (list): 模型生成的主題列表。

        Returns:
            (int, str): (分數, 理由)
        """
        prompt_template = """You are a sharp public health analyst. Your task is to evaluate the RELEVANCE of a list of "Generated Aspects" by comparing it to a "Ground Truth Aspects" list from a pandemic press briefing.

        Instructions:
        1. Review the "Ground Truth Aspects" which are considered the most important topics.
        2. Review the "Generated Aspects".
        3. Evaluate how well the generated list covers the key topics from the ground truth list.
        4. **Crucially, consider both the topic coverage AND the total number of aspects.** An ideal list is not only relevant but also matches the granularity (i.e., the number of topics) of the ground truth list.

        Scoring Criteria:
        - 5 (Excellent): The generated list perfectly aligns in **both topic coverage and quantity**. It covers all or nearly all ground truth topics, and the number of aspects is nearly identical (e.g., differs by no more than 1).
        - 4 (Good): The list shows a strong correspondence but has a minor flaw. It either covers all topics but with a slightly different quantity (e.g., splits one topic into two), OR it matches the quantity perfectly but misses one minor topic.
        - 3 (Fair): The list captures some key topics but has noticeable flaws. It might miss several important topics, **OR** the number of aspects is significantly different (too many or too few), indicating a mismatch in granularity.
        - 2 (Poor): The list is largely irrelevant. It misses most key topics **and/or** the number of aspects is vastly different, often being bloated with minor details.
        - 1 (Very Poor): The generated list is completely off-topic and fails on both relevance and appropriate granularity.

        Ground Truth Aspects:
        ---
        {gt_aspects}
        ---

        Generated Aspects to Evaluate:
        ---
        {gen_aspects}
        ---

        Please provide your rating first, followed by a brief reason.
        
        Return Format: [Number]. [Reason]

        Example Response: 3. The generated list covers the new variants and vaccination rates, but it completely misses the topic of misinformation and is fragmented into too many small points.
        """
        # 將 list 轉換為帶有項目符號的字串，方便模型閱讀
        gt_str = "\n".join(f"- {item}" for item in ground_truth_aspects)
        gen_str = "\n".join(f"- {item}" for item in generated_aspects)

        prompt = prompt_template.format(gt_aspects=gt_str, gen_aspects=gen_str)
        return self.get_score_and_reason(prompt)

def load_json_files(root_dir: str) -> list:
    # return ["../Result/langgraph/no_memory/gemini_filtered_data_y6n6/gemini-2.5-flash-lite/6_sample_28.json"]
    """
    遞迴地掃描指定根目錄，並返回所有未被評估過的 .json 檔案的路徑列表。
    這個版本會明確排除 'Chat_eval' 目錄，並且會跳過已經生成過對應輸出檔案的原始檔案。
    
    Args:
        root_dir (str): 要掃描的根目錄路徑。
        
    Returns:
        list: 一個包含所有待處理 .json 檔案完整路徑的列表。
    """
    json_file_paths = []
    output_dir_name = 'Chat_eval'
    output_root_dir = os.path.join(root_dir, output_dir_name) # 先組合好輸出的根目錄

    # print(f"Scanning for .json files in '{root_dir}', excluding processed files...")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        
        # (不變) 排除輸出目錄，避免掃描
        if output_dir_name in dirnames:
            dirnames.remove(output_dir_name)
            
        for filename in filenames:
            if filename.endswith('.json') and 'sample' in filename:
                full_path = os.path.join(dirpath, filename)
                
                # --- 【核心修改】 ---
                # 1. 根據找到的原始檔案路徑，計算出它對應的輸出檔案路徑應該是什麼
                relative_path = os.path.relpath(full_path, root_dir)
                expected_output_path = os.path.join(output_root_dir, relative_path)
                
                # 2. 檢查這個預期的輸出檔案是否已經存在
                if not os.path.exists(expected_output_path):
                    # 3. 只有當輸出檔案不存在時，才將原始檔案加入待處理列表
                    json_file_paths.append(full_path)
                # else:
                #     print(f"Skipping '{full_path}' as its output already exists.")

    return json_file_paths


def calculate_aspect_bertscore(
    scorer: BERTScorer, 
    valid_generated_aspects: list, 
    valid_reference_aspects: list, 
    total_num_pairs: int
) -> tuple[float, float]:
    """
    計算配對好的 aspect name 之間的兩種 BERTScore F1 平均分。

    Args:
        scorer (BERTScorer): 預初始化的 BERTScorer 實例。
        valid_generated_aspects (list): 已過濾的、有效的生成主題名稱列表。
        valid_reference_aspects (list): 已過濾的、有效的參考主題名稱列表。
        total_num_pairs (int): 原始的總配對數量。

    Returns:
        A tuple containing (strict_average, penalized_average).
    """
    valid_num_pairs = len(valid_generated_aspects)

    if valid_num_pairs == 0:
        return 0.0, 0.0

    # Step 1: 為有效配對計算分數
    try:
        _, _, f1_scores = scorer.score(valid_generated_aspects, valid_reference_aspects)
        score_sum = f1_scores.sum().item()
    except Exception as e:
        print(f"An error occurred during BERTScore calculation: {e}")
        return 0.0, 0.0

    # Step 2: 計算兩種平均分
    # 嚴格平均分：只考慮有效配對
    strict_average = score_sum / valid_num_pairs
    
    # 懲罰平均分：用總配對數作為分母
    # 確保 total_num_pairs 不為 0，儘管在主流程中已保證
    penalized_average = score_sum / total_num_pairs if total_num_pairs > 0 else 0.0

    return strict_average, penalized_average
    
def main():
    # 設定包含所有模型結果的根目錄
    root_directory = '../Result'
    files_to_process = load_json_files(root_directory)
    
    if not files_to_process:
        print("No new JSON files to evaluate.")
        return
        
    print(f"Found {len(files_to_process)} JSON file(s) to evaluate.")
    # print(1/0)
    
    evaluator = ChatEval(model_name='gpt-4-turbo')
    device = 'cuda:1' if torch.cuda.is_available() else 'cpu'
    # print(f"Using device: {device} for BERTScore calculation.")
    bert_scorer = BERTScorer(model_type="microsoft/deberta-v3-large", lang="en", device=device)


    for input_filepath in tqdm(files_to_process):
        print(f"\n--- Processing file: {input_filepath} ---")

        # ... (檔案讀取和路徑設定不變) ...
        new_root_dir = os.path.join(root_directory, 'Chat_eval')
        relative_path = os.path.relpath(input_filepath, root_directory)
        output_filepath = os.path.join(new_root_dir, relative_path)
        output_dir = os.path.dirname(output_filepath)
        os.makedirs(output_dir, exist_ok=True)
        
        try:
            with open(input_filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading or decoding {input_filepath}: {e}")
            continue

        # --- 核心邏輯：準備所有評估所需的、已正確配對的資料 ---
        
        # 1. 提取所有資料片段
        generated_summary_dict = data.get('generated_revised_aspects_summary', {})
        if not generated_summary_dict:
            generated_summary_dict = data.get('generated_prompt_aspect_summary', {})

        if not generated_summary_dict:
            print(f"Warning: No generated summaries found in {input_filepath}. Skipping file.")
            continue

        ground_truth_summary_dict = data.get('ground_truth_aspect_summary', {})
        pairing_dict = data.get('pairing', {})

        ground_truth_aspects = list(ground_truth_summary_dict.keys())
        generated_aspects = list(generated_summary_dict.keys())

        # 2. 建立反向查找字典 (summary -> aspect name)
        gen_summary_to_aspect = {v: k for k, v in generated_summary_dict.items()}
        gt_summary_to_aspect = {v: k for k, v in ground_truth_summary_dict.items()}
        
        # 3. 從 pairing 取得有序的摘要列表
        generated_summaries_ordered = pairing_dict.get('generated', [])
        ground_truth_summaries_ordered = pairing_dict.get('ground_truth', [])
        
        total_pairs = len(generated_summaries_ordered)


        # 4. 準備用於 BERTScore 的「有效配對」列表
        valid_generated_aspects = []
        valid_ground_truth_aspects = []
        
        for gen_summary, gt_summary in zip(generated_summaries_ordered, ground_truth_summaries_ordered):
            # 有效配對的條件是：雙方的摘要內容都不能為空
            if (gen_summary and gen_summary.strip()) and (gt_summary and gt_summary.strip()):
                gen_aspect = gen_summary_to_aspect.get(gen_summary)
                gt_aspect = gt_summary_to_aspect.get(gt_summary)
                
                if gen_aspect and gt_aspect:
                    valid_generated_aspects.append(gen_aspect)
                    valid_ground_truth_aspects.append(gt_aspect)

        


        # --- 開始評估 ---

        # 1. 評估 Factuality (獨立評估所有生成摘要的真實性)
        # print("Evaluating Factuality...")
        document = data.get('document', '')
        full_generated_summary_str = "\n\n".join(f"**{k}**\n{v}" for k, v in generated_summary_dict.items())
        factuality_score, factuality_reason = evaluator.evaluate_factuality(document, full_generated_summary_str)


        # 2. 評估 Relevance (使用 pairing 找到的所有 aspect name 進行評估，即使是無效配對的)
        # 這裡需要一個完整的、帶有空值的列表來評估模型是否生成了不該生成的東西
        # 這部分邏輯比較複雜，我們先專注在 BERTScore 上，此處暫時使用 valid list
        # 如果需要更複雜的 Relevance 評估，我們可以再調整
        # print("Evaluating Relevance (on valid pairs)...")
        relevance_score, relevance_reason = evaluator.evaluate_relevance(ground_truth_aspects, generated_aspects)


        # 3. 計算 Aspect Name 的 BERTScore
        # print("Calculating Paired Aspect Name BERTScores...")
        # print(f"Valid_generated_aspects: {valid_generated_aspects}")
        # print(f"Valid_ground_truth_aspects: {valid_ground_truth_aspects}")

        strict_avg, penalized_avg = calculate_aspect_bertscore(
            bert_scorer,
            valid_generated_aspects,
            valid_ground_truth_aspects,
            total_pairs
        )
        # print(f"BERTScore F1 (Strict Avg): {strict_avg:.4f}")
        # print(f"BERTScore F1 (Penalized Avg): {penalized_avg:.4f}")

        # 4. 寫入所有分數
        if 'metrics' not in data:
            data['metrics'] = {}
        data['metrics']['factuality_score'] = factuality_score
        data['metrics']['factuality_reason'] = factuality_reason
        data['metrics']['relevance_score'] = relevance_score
        data['metrics']['relevance_reason'] = relevance_reason
        data['metrics']['paired_aspect_bertscore_strict_avg'] = strict_avg
        data['metrics']['paired_aspect_bertscore_penalized_avg'] = penalized_avg
        
        # 5. 寫入檔案
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        # print(f"Evaluation complete. Results saved to '{output_filepath}'")

        # print(1/0)  # 故意觸發錯誤以測試除錯


if __name__ == '__main__':
    main()