import pandas as pd
from rouge_score import rouge_scorer
from bert_score import BERTScorer
import json
import numpy as np
from scipy.optimize import linear_sum_assignment
from tqdm import tqdm

import torch
import pynvml

def get_available_gpu(threshold=0.9):
    pynvml.nvmlInit()
    available_gpus = []
    device_count = pynvml.nvmlDeviceGetCount()

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)

        total = meminfo.total
        used = meminfo.used
        free = meminfo.free

        if free / total > threshold:
            available_gpus.append(i)

    pynvml.nvmlShutdown()
    return available_gpus


# Function for calculating ROUGE scores
def calculate_rouge(predicted, ground_truth):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(ground_truth, predicted)
    return scores['rouge1'].fmeasure, scores['rouge2'].fmeasure, scores['rougeL'].fmeasure

# Function to calculate BERTScore for reference and generated summaries
def calculate_bertscore(reference_summaries, generated_summaries):
    device_ = "cuda:0"
    
    scorer = BERTScorer(model_type="microsoft/deberta-v3-large", lang="en", device=device_)
    
    P, R, F1 = scorer.score(generated_summaries, reference_summaries)
    
    bert_results = []
    for p, r, f1 in zip(P, R, F1):
        result = {
            'BERTScore Precision': p.item(),
            'BERTScore Recall': r.item(),
            'BERTScore F1': f1.item(),
        }
        bert_results.append(result)
    
    return pd.DataFrame(bert_results)

# Main function to find the optimal matching and calculate evaluation metrics
def evaluate_summary(ground_truth, predicted) -> dict:
    if not ground_truth or not predicted:
        return {}

    # Padding if necessary
    max_length = max(len(ground_truth), len(predicted))

    abs_aspect_diff = abs(len(predicted) - len(ground_truth))  # Difference in aspect counts
    
    # Pad ground truth and predicted summaries to the same length by adding empty summaries
    while len(ground_truth) < max_length:
        ground_truth.append("")  # Padding empty summary for ground truth
    
    while len(predicted) < max_length:
        predicted.append("")  # Padding empty summary for predicted

    # Create similarity (cost) matrix for the matching problem
    cost_matrix = np.zeros((len(predicted), len(ground_truth)))

    for i, p in enumerate(predicted):
        for j, g in enumerate(ground_truth):
            if p == "" or g == "":
                cost_matrix[i, j] = 0  # Padding summaries have 0 similarity
            else:
                # Calculate BERTScore
                bert_score_df = calculate_bertscore([g], [p])  # Wrap in list to handle one-to-one pair
                bert_score = bert_score_df['BERTScore F1'][0]  # Get the mean F1 score
                
                # Calculate ROUGE scores
                rouge1, rouge2, rougeL = calculate_rouge(p, g)

                # Combine BERTScore and ROUGE scores into a single metric
                total_score = bert_score + rouge1 + rouge2 + rougeL

                # Store the total score as the cost (negative for maximization problem)
                cost_matrix[i, j] = total_score

    # Use Hungarian algorithm to find the optimal matching
    row_ind, col_ind = linear_sum_assignment(cost_matrix, maximize=True)

    # Retrieve the best matching based on Hungarian algorithm
    best_pairing = [(predicted[i], ground_truth[j]) for i, j in zip(row_ind, col_ind)]

    # Calculate total metrics for the best pairing
    total_bert, total_rouge1, total_rouge2, total_rougeL = 0, 0, 0, 0
    for i, j in zip(row_ind, col_ind):
        p, g = predicted[i], ground_truth[j]
        if p != "" and g != "":
            # BERTScore
            bert_score_df = calculate_bertscore([g], [p])
            total_bert += bert_score_df['BERTScore F1'][0]

            # ROUGE scores
            rouge1, rouge2, rougeL = calculate_rouge(p, g)
            total_rouge1 += rouge1
            total_rouge2 += rouge2
            total_rougeL += rougeL

    # Average the ROUGE scores across all pairings
    num_pairings = len(row_ind)
    average_bert_score = total_bert / num_pairings
    average_rouge1 = total_rouge1 / num_pairings
    average_rouge2 = total_rouge2 / num_pairings
    average_rougeL = total_rougeL / num_pairings

    # Return the best matching pairing and metrics in JSON format
    result = {
        'pairing': {
            'generated': [pair[0] for pair in best_pairing],
            'ground_truth': [pair[1] for pair in best_pairing]
        },
        'metrics': {
            'BERTScore': average_bert_score,
            'ROUGE-1': average_rouge1,
            'ROUGE-2': average_rouge2,
            'ROUGE-L': average_rougeL,
            '#AbsAspDiff': abs_aspect_diff
        }
    }
    
    return result

# Example usage
# ground_truth_example = [
#       "Q2 2024 revenue reached $455.3 million, a 7.5% increase quarter-over-quarter and a 14.2% increase year-over-year. These results slightly exceeded the internal guidance of $440 to $450 million issued in Q1 2024. The outperformance was primarily driven by stronger-than-anticipated adoption of the new \"SynergyAI\" platform in the North American market, coupled with a rebound in enterprise spending in the APAC region.",
#     #   "Actual CapEx for Q3 totaled $475 million, slightly below the internal target of $500 million due to project phasing delays in the European renewable energy infrastructure buildout. The full-year CapEx guidance is revised downwards to $1.95 billion to $2.1 billion, reflecting these delays, efficiency gains, and strategic prioritization. The long-term CapEx outlook remains robust, with significant investments planned for 2025 and beyond, including a new semiconductor manufacturing facility in the United States.",
#     #   "The LTA portfolio includes 127 active agreements, accounting for about 42% of revenue. The average remaining term is 3.2 years, with a median contract value of $7.5 million annually. The overall LTA utilization rate was 88.5%, resulting in $4.8 million in underutilization charges, an increase from $4.45 million in the previous quarter. The renewal rate remains strong at 91%, but the company is focused on addressing underutilization issues, especially in Europe. Customer LTA optimization is being implemented to proactively identify potential issues and develop mitigation plans.",
#     #   "The Renewable Energy Advancement Program (REAP) disbursed $2.7 billion in Q3, a 12% increase year-over-year. Project Helios in Nevada secured a $150 million REAP grant. The IRS issued approximately $450 million in tax refunds related to renewable energy projects in Q3, with solar projects accounting for the largest share.",
#     #   "There was a moderate increase in inventory levels and a corresponding rise in Days of Inventory (DOI) this quarter. Total inventory value at the end of Q3 was $78.5 million, up from $72.3 million in Q2. Consolidated DOI increased to 72 days from 66 days in Q2. This increase is within the projected range but warrants close monitoring due to regional variations and supply chain fluctuations. The implementation of the new inventory management system, \"Project Zenith,\" has also caused some initial disruptions, but the company is optimistic about its long-term benefits. They expect inventory levels and DOI to normalize gradually over the next couple of quarters.",
#     #   "The company anticipates Q3 2024 revenue to be in the range of $115 million to $120 million, representing a growth of 8% to 12% compared to Q3 2023. Gross margin is projected to be between 62% and 64%, a slight improvement compared to the 61.5% realized in Q3 2023. This growth and margin improvement are driven by expansion in the enterprise segment and the successful launch of the \"Synergy AI\" add-on.",
#     #   "The company is implementing a phased expansion across three core fabs: Fab A in the USA, Fab B in Taiwan, and Fab C in Germany. This plan focuses on optimizing existing infrastructure through advanced process node migration, equipment upgrades, and targeted cleanroom expansions. They anticipate a 12% overall increase in wafer output by Q4 2024. The total investment is $380 million, funded through existing cash reserves and projected operating cash flow.",
#     #   "The LTA utilization rate was 88.5%. The company did not provide utilization rate guidance for the next quarter. The company's goal is to achieve a sustained utilization rate of 80% to 82% by 2026."
#     ]

# predicted_example = [
#       "Q2 2024 revenue reached $455.3 million, a 7.5% increase QoQ and a 14.2% increase YoY. This exceeded the previous guidance of $440-$450 million due to stronger-than-expected adoption of the \"SynergyAI\" platform in North America and a rebound in enterprise spending in the APAC region.",
#     #   "Full-year CapEx guidance was revised downwards to $1.95 - $2.1 billion, from a previous internal target of $500 million for Q3, due to project phasing delays in European renewable energy infrastructure. Despite this, the long-term CapEx outlook remains robust, with significant investments planned for 2025 and beyond, including a new semiconductor facility in the US.",
#     #   "The overall LTA utilization rate was 88.5% in Q3, slightly below the 92% target, resulting in $4.8 million in underutilization charges (up from $4.45 million last quarter). Focus is on addressing underutilization, particularly in Europe. The company aims for a sustained utilization rate of 80-82% by 2026.",
#     #   "Government support was strong, with the Renewable Energy Advancement Program (REAP) disbursing $2.7 billion in Q3, a 12% YoY increase. Project Helios secured a $150 million REAP grant. The Inflation Reduction Act's direct pay provision resulted in approximately $450 million in tax refunds for renewable energy projects, primarily solar.",
#     #   "",
#     #   "Actual CapEx for Q3 totaled $475 million, slightly below the $500 million internal target due to project phasing delays. Key investment areas include technology infrastructure, manufacturing capacity expansion, and renewable energy projects. A $380 million investment is planned for fab expansions (Fab A, B, and C).",
#     #   "The call mentions expansion of existing fabs (Fab A, B, and C) through process node migration, equipment upgrades, and cleanroom expansions. A new semiconductor manufacturing facility in the United States is planned, but no specific construction progress was detailed for this quarter.",
#     #   "Net margin and Diluted EPS results were not explicitly discussed in the provided transcript."
#     ]

# # Get evaluation
# evaluation_result = evaluate_summary(ground_truth_example, predicted_example)
# print(evaluation_result)
