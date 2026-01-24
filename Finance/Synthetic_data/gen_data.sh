#!/bin/bash

MAX_RETRIES=3
MAX_PARALLEL_JOBS=1
FAILED_JOBS_FILE="failed_data_jobs.txt"
> "$FAILED_JOBS_FILE"

run_with_retry() {
  local cmd="$1"
  local attempt=1
  local success=0

  while [ $attempt -le $MAX_RETRIES ]; do
    echo "🚀 Running: $cmd (Attempt $attempt)"
    $cmd  
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

JOBS=(
  "python data_generation_gemini.py --num_sample 9 --num_aspect 5"
  "python data_generation_gemini.py --num_sample 5 --num_aspect 6"
  "python data_generation_gemini.py --num_sample 9 --num_aspect 8"
)

printf "%s\n" "${JOBS[@]}" | xargs -P $MAX_PARALLEL_JOBS -I {} bash -c 'run_with_retry "{}"' _

echo ""
if [ -s "$FAILED_JOBS_FILE" ]; then
  echo "❗ The following jobs failed after $MAX_RETRIES attempts:"
  cat "$FAILED_JOBS_FILE"
  exit 1
else
  echo "🎉 All jobs completed successfully"
  exit 0
fi
