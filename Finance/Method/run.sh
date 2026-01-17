#!/bin/bash

MAX_RETRIES=3
MAX_PARALLEL_JOBS=5  # 同時執行幾個實驗
FAILED_JOBS_FILE="failed_jobs.txt"
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
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 2 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 2 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 0 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 2 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 2 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 0 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 4 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 4 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 0 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 4 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 4 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 0 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 6 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 6 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o-mini --y 0 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 6 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 6 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode direct --model gpt-4o --y 0 --n 6 --provide_aspect_num --aspect_source csv"

"python prompt.py --cot_mode cot --model gpt-4o-mini --y 2 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 2 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 0 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 2 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 2 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 0 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 4 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 4 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 0 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 4 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 4 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 0 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 6 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 6 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o-mini --y 0 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 6 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 6 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot --model gpt-4o --y 0 --n 6 --provide_aspect_num --aspect_source csv"

"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 2 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 2 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 0 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 2 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 2 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 0 --n 2 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 4 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 4 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 0 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 4 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 4 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 0 --n 4 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 6 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 6 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o-mini --y 0 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 6 --n 6 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 6 --n 0 --provide_aspect_num --aspect_source csv"
"python prompt.py --cot_mode cot_sc --model gpt-4o --y 0 --n 6 --provide_aspect_num --aspect_source csv"

# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 2 --n 2"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 2 --n 0"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 0 --n 2"
# "python langgraph_guided.py --memory False --model gpt-4o --y 2 --n 2"
# "python langgraph_guided.py --memory False --model gpt-4o --y 2 --n 0"
# "python langgraph_guided.py --memory False --model gpt-4o --y 0 --n 2"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 4 --n 4"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 4 --n 0"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 0 --n 4"
# "python langgraph_guided.py --memory False --model gpt-4o --y 4 --n 4"
# "python langgraph_guided.py --memory False --model gpt-4o --y 4 --n 0"
# "python langgraph_guided.py --memory False --model gpt-4o --y 0 --n 4"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 6 --n 6"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 6 --n 0"
# "python langgraph_guided.py --memory False --model gpt-4o-mini --y 0 --n 6"
# "python langgraph_guided.py --memory False --model gpt-4o --y 6 --n 6"
# "python langgraph_guided.py --memory False --model gpt-4o --y 6 --n 0"
# "python langgraph_guided.py --memory False --model gpt-4o --y 0 --n 6"
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
