#!/bin/bash
# gen_all_categories.sh
# Batch script to generate synthetic earnings call transcripts for all 20 company categories

set -e

# Configuration
MAX_RETRIES=3
MAX_PARALLEL_JOBS=2  # Number of parallel jobs (adjust based on API rate limits)
FAILED_JOBS_FILE="failed_category_jobs.txt"
NUM_SAMPLES=50       # Number of samples per category (10 each for 4,5,6,7,8 aspects)
# MODEL="google/gemini-2.0-flash-001"  # OpenRouter model format
MODEL="x-ai/grok-4.1-fast"
OUTPUT_DIR="output"
TEMPLATES_DIR="industry_templates"
DELAY=1.0            # Delay between samples in seconds

# Clear/create failed jobs log
> "$FAILED_JOBS_FILE"

# All 20 company categories
CATEGORIES=(
    # Technology
    "software_saas"
    "cloud_computing"
    "ecommerce"
    "cybersecurity"
    # Energy
    "oil_gas"
    "renewable_energy"
    "utilities"
    # Financial
    "banking"
    "insurance"
    "asset_management"
    # Healthcare
    "pharma_biotech"
    "medical_devices"
    "healthcare_services"
    # Consumer
    "consumer_goods"
    "retail"
    "food_beverage"
    # Industrial
    "automotive"
    "aerospace_defense"
    "manufacturing"
    # Telecom
    "telecom"
)

# Function to run a category with retries
run_with_retry() {
    local category="$1"
    local attempt=1
    local success=0
    
    while [ $attempt -le $MAX_RETRIES ]; do
        echo "🚀 Generating data for: $category (Attempt $attempt/$MAX_RETRIES)"
        
        python data_generation_multi_category.py \
            --category "$category" \
            --num_sample $NUM_SAMPLES \
            --model "$MODEL" \
            --output_dir "$OUTPUT_DIR" \
            --templates_dir "$TEMPLATES_DIR" \
            --delay $DELAY
        
        if [ $? -eq 0 ]; then
            echo "✅ Success: $category"
            success=1
            break
        else
            echo "❌ Failed: $category (Attempt $attempt)"
            attempt=$((attempt + 1))
            sleep 30  # Wait before retry
        fi
    done
    
    if [ $success -eq 0 ]; then
        echo "$category" >> "$FAILED_JOBS_FILE"
    fi
}

export -f run_with_retry
export MAX_RETRIES
export FAILED_JOBS_FILE
export NUM_SAMPLES
export MODEL
export OUTPUT_DIR
export TEMPLATES_DIR
export DELAY

# Print configuration
echo "=============================================="
echo "Synthetic Data Generation - All Categories"
echo "=============================================="
echo "Model: $MODEL"
echo "Samples per category: $NUM_SAMPLES"
echo "Aspect distribution: 10 samples each for 4, 5, 6, 7, 8 aspects"
echo "Parallel jobs: $MAX_PARALLEL_JOBS"
echo "Categories: ${#CATEGORIES[@]}"
echo "Total samples to generate: $((${#CATEGORIES[@]} * NUM_SAMPLES))"
echo "=============================================="
echo ""

# Check if templates exist
if [ ! -d "$TEMPLATES_DIR" ]; then
    echo "⚠️  Warning: Templates directory '$TEMPLATES_DIR' does not exist."
    echo "   Run 'python generate_industry_templates.py --all' first to generate templates."
    echo "   Or press Enter to continue with default templates..."
    read -r
fi

# Run all categories
if [ $MAX_PARALLEL_JOBS -gt 1 ]; then
    # Parallel execution
    printf "%s\n" "${CATEGORIES[@]}" | xargs -P $MAX_PARALLEL_JOBS -I {} bash -c 'run_with_retry "$@"' _ {}
else
    # Sequential execution
    for category in "${CATEGORIES[@]}"; do
        run_with_retry "$category"
        sleep 5  # Brief pause between categories
    done
fi

# Report results
echo ""
echo "=============================================="
echo "Generation Complete"
echo "=============================================="

if [ -s "$FAILED_JOBS_FILE" ]; then
    echo "❗ The following categories failed after $MAX_RETRIES attempts:"
    cat "$FAILED_JOBS_FILE"
    echo ""
    echo "To retry failed categories, run:"
    echo "  cat $FAILED_JOBS_FILE | xargs -I {} python data_generation_multi_category.py --category {}"
    exit 1
else
    echo "🎉 All categories completed successfully!"
    
    # Count generated files
    total_files=$(find "$OUTPUT_DIR" -name "*.json" 2>/dev/null | wc -l)
    echo "📊 Total samples generated: $total_files"
    exit 0
fi
