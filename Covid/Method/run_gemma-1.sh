#!/bin/bash

MAX_RETRIES=10
MAX_PARALLEL_JOBS=1  # 同時執行幾個實驗
FAILED_JOBS_FILE="failed_jobs_gemma-1.txt"
> "$FAILED_JOBS_FILE"

run_with_retry() {
  local cmd="$1"
  local attempt=1
  local success=0

  while [ $attempt -le $MAX_RETRIES ]; do
    echo "🚀 Running: $cmd (Attempt $attempt)"
    eval $cmd
    if [ $? -eq 0 ]; then
      echo "✅ Success: $cmd"
      success=1
      break
    else
      echo "❌ Failed: $cmd"
      attempt=$((attempt + 1))
      sleep 60
    fi
  done

  if [ $success -eq 0 ]; then
    echo "$cmd" >> "$FAILED_JOBS_FILE"
  fi
}

export -f run_with_retry
export MAX_RETRIES
export FAILED_JOBS_FILE

# === 所有實驗組合 ===
JOBS=(
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 2 --n 2 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 2 --n 0 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 0 --n 2 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 2 --n 2 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 2 --n 0 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 0 --n 2 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 4 --n 4 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 4 --n 0 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 0 --n 4 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 4 --n 4 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 4 --n 0 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 0 --n 4 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 6 --n 6 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 6 --n 0 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-12b-it --y 0 --n 6 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 6 --n 6 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 6 --n 0 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gemma-3-27b-it --y 0 --n 6 --gemini_api_key GEMINI_API_KEY0 --provide_aspect_num --aspect_source csv"

"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 2 --n 2 --gemini_api_key GEMINI_API_KEY_NYCU"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 2 --n 0 --gemini_api_key GEMINI_API_KEY4"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 0 --n 2 --gemini_api_key GEMINI_API_KEY"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 2 --n 2 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 2 --n 0 --gemini_api_key GEMINI_API_KEY_ADSL"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 0 --n 2 --gemini_api_key GEMINI_API_KEY_NYCU"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 4 --n 4 --gemini_api_key GEMINI_API_KEY5"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 4 --n 0 --gemini_api_key GEMINI_API_KEY"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 0 --n 4 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 4 --n 4 --gemini_api_key GEMINI_API_KEY_ADSL"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 4 --n 0 --gemini_api_key GEMINI_API_KEY_NYCU"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 0 --n 4 --gemini_api_key GEMINI_API_KEY6"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 6 --n 6 --gemini_api_key GEMINI_API_KEY"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 6 --n 0 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot --model gemma-3-12b-it --y 0 --n 6 --gemini_api_key GEMINI_API_KEY_ADSL"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 6 --n 6 --gemini_api_key GEMINI_API_KEY_NYCU"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 6 --n 0 --gemini_api_key GEMINI_API_KEY7"
"python prompt.py --cot_mode cot --model gemma-3-27b-it --y 0 --n 6 --gemini_api_key GEMINI_API_KEY"

"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 2 --n 2 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 2 --n 0 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 0 --n 2 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 2 --n 2 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 2 --n 0 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 0 --n 2 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 4 --n 4 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 4 --n 0 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 0 --n 4 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 4 --n 4 --gemini_api_key GEMINI_API_KEY"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 4 --n 0 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 0 --n 4 --gemini_api_key GEMINI_API_KEY_ADSL"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 6 --n 6 --gemini_api_key GEMINI_API_KEY_NYCU"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 6 --n 0 --gemini_api_key GEMINI_API_KEY0"
"python prompt.py --cot_mode cot_sc --model gemma-3-12b-it --y 0 --n 6 --gemini_api_key GEMINI_API_KEY_BRYANT"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 6 --n 6 --gemini_api_key GEMINI_API_KEY_ADSL"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 6 --n 0 --gemini_api_key GEMINI_API_KEY_NYCU"
"python prompt.py --cot_mode cot_sc --model gemma-3-27b-it --y 0 --n 6 --gemini_api_key GEMINI_API_KEY1"

"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 2 --n 2 --api_key GEMINI_API_KEY"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 2 --n 0 --api_key GEMINI_API_KEY"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 0 --n 2 --api_key GEMINI_API_KEY_ADSL"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 2 --n 2 --api_key GEMINI_API_KEY_NYCU"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 2 --n 0 --api_key GEMINI_API_KEY2"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 0 --n 2 --api_key GEMINI_API_KEY"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 4 --n 4 --api_key GEMINI_API_KEY_BRYANT"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 4 --n 0 --api_key GEMINI_API_KEY_ADSL"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 0 --n 4 --api_key GEMINI_API_KEY_NYCU"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 4 --n 4 --api_key GEMINI_API_KEY3"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 4 --n 0 --api_key GEMINI_API_KEY"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 0 --n 4 --api_key GEMINI_API_KEY_BRYANT"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 6 --n 6 --api_key GEMINI_API_KEY_ADSL"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 6 --n 0 --api_key GEMINI_API_KEY_NYCU"
"python langgraph_guided.py --memory False --model gemma-3-12b-it --y 0 --n 6 --api_key GEMINI_API_KEY4"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 6 --n 6 --api_key GEMINI_API_KEY"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 6 --n 0 --api_key GEMINI_API_KEY_BRYANT"
"python langgraph_guided.py --memory False --model gemma-3-27b-it --y 0 --n 6 --api_key GEMINI_API_KEY_ADSL"
)

# === 執行所有實驗（平行）===
printf "%s\n" "${JOBS[@]}" | xargs -P $MAX_PARALLEL_JOBS -I {} bash -c 'run_with_retry "$@"' _ {}

# === 最後報告 ===
echo ""
if [ -s "$FAILED_JOBS_FILE" ]; then
  echo "❗ The following jobs failed after $MAX_RETRIES attempts:"
  cat "$FAILED_JOBS_FILE"
  exit 1
else
  echo "🎉 All jobs completed successfully"
  exit 0
fi
