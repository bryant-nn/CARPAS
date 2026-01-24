import json
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, Dataset
from transformers import AutoModel, AutoTokenizer, DataCollatorWithPadding, get_linear_schedule_with_warmup
from tqdm import tqdm
import numpy as np
import os
from torch.utils.tensorboard import SummaryWriter
import argparse
import random

import torch.multiprocessing as mp
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler

from peft import get_peft_model, LoraConfig, TaskType, PeftModel

def set_seed(seed: int = 42):
    """Sets the seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

# === 1. Configuration Management ===
class Config:
    model_name = "Qwen/Qwen3-Embedding-0.6B"
    data_base_dir = "../../Synthetic_data/"
    train_pointer_file = os.path.join(data_base_dir, "train.json")
    valid_pointer_file = os.path.join(data_base_dir, "valid.json")
    test_pointer_file = os.path.join(data_base_dir, "test.json")
    output_dir = "./trained_model_aspect_regression"
    batch_size = 1
    learning_rate = 2e-5
    num_epochs = 30
    max_length = 768 #768
    patience = 30

# === 2. Data Loading Logic ===
# NEW FUNCTION: Loads data by reading a pointer file containing relative paths
def load_data_from_pointer_file(pointer_file_path: str, base_dir: str) -> list[dict]:
    """
    Reads a JSON file containing a list of relative paths, then loads the data
    from each of those paths.
    """
    print(f"Loading pointer file from: {pointer_file_path}")
    with open(pointer_file_path, 'r', encoding='utf-8') as f:
        relative_paths = json.load(f)

    samples = []
    print(f"Loading {len(relative_paths)} data files...")
    for rel_path in tqdm(relative_paths, desc=f"Processing {os.path.basename(pointer_file_path)}"):
        # Construct the full path to the actual data file
        full_path = os.path.join(base_dir, rel_path)
        try:
            with open(full_path, 'r', encoding='utf-8') as f_data:
                data = json.load(f_data)
            
            document = data.get("document")
            # The label is the NUMBER of aspects
            aspect_count = len(data.get("aspects", []))
            
            if document:
                samples.append({
                    "document": document, 
                    "label": aspect_count,
                    "source_file": full_path
                    })
        except Exception as e:
            print(f"Warning: Skipping file {full_path} due to error: {e}")
            continue
            
    return samples

# MODIFIED: This class is now more general and works with the pre-loaded samples
class AspectDataset(Dataset):
    """Prepares dataset for aspect count prediction."""
    def __init__(self, samples: list[dict], tokenizer: AutoTokenizer, max_length: int):
        self.samples = samples
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        item = self.samples[idx]
        document = item['document']
        label = item['label']
        source_file = item['source_file']

        inputs = self.tokenizer(
            document, 
            truncation=True, 
            max_length=self.max_length,
        )

        return {
            'input_ids': inputs['input_ids'],
            'attention_mask': inputs['attention_mask'],
            'labels': torch.tensor(label, dtype=torch.float32),
            'source_file': source_file
        }

# === 3. Model with Regression Head (Unchanged) ===
class AspectCountModel(nn.Module):
    def __init__(self, model_name):
        super().__init__()
        self.transformer = AutoModel.from_pretrained(model_name, trust_remote_code=True)
        hidden_size = self.transformer.config.hidden_size
        self.dropout = nn.Dropout(0.1)
        # self.regressor = nn.Linear(hidden_size, 1)
        self.regressor = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size // 2, 1)
        )

    def _mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output.last_hidden_state
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        return sum_embeddings / sum_mask

    def forward(self, input_ids, attention_mask):
        outputs = self.transformer(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = self._mean_pooling(outputs, attention_mask)
        pooled_output = self.dropout(pooled_output)
        logits = self.regressor(pooled_output)
        return logits.squeeze(-1)

class CustomDataCollator:
    def __init__(self, data_collator):
        self.data_collator = data_collator

    def __call__(self, features):
        source_files = [f.pop("source_file") for f in features]
        
        #   (input_ids, attention_mask, labels)
        batch = self.data_collator(features)
        
        batch["source_file"] = source_files
        
        return batch

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group("nccl", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

# === 4. Training and Evaluation Logic (Unchanged) ===
def train_epoch(model, dataloader, optimizer, scheduler, loss_fn, device, writer, global_step, rank):
    model.train()
    running_loss = 0.0
    # loop = tqdm(dataloader, desc="Training", dynamic_ncols=True)
    loop = tqdm(dataloader, desc="Training", dynamic_ncols=True, disable=(rank != 0))

    for batch in loop:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        optimizer.zero_grad()
        predictions = model(input_ids=input_ids, attention_mask=attention_mask)
        loss = loss_fn(predictions, labels)
        loss.backward()
        optimizer.step()
        scheduler.step()
        # loop.set_postfix(loss=loss.item())
        
        # ADDED: Log training loss for each step to TensorBoard
        # writer.add_scalar('Loss/train_step', loss.item(), global_step)
        if rank == 0:
            loop.set_postfix(loss=loss.item())
            writer.add_scalar('Loss/train_step', loss.item(), global_step)

        global_step += 1
        running_loss += loss.item()
        
    return running_loss / len(dataloader), global_step

def evaluate(model, dataloader, loss_fn, device, desc="Evaluating", rank=0, mode='val'):
    model.eval()
    running_loss = 0.0
    all_predictions, all_labels = [], []
    all_source_files = []
    accuracy_count = 0
    with torch.no_grad():
        # loop = tqdm(dataloader, desc=desc, dynamic_ncols=True)
        loop = tqdm(dataloader, desc=desc, dynamic_ncols=True, disable=(rank != 0))

        for batch in loop:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            source_files = batch['source_file'] 

            predictions = model(input_ids=input_ids, attention_mask=attention_mask)
            loss = loss_fn(predictions, labels)

            running_loss += loss.item()
            all_predictions.extend(predictions.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
            all_source_files.extend(source_files)

            # --- ADDED: Compute accuracy ---
            
            preds = np.round(predictions.cpu().numpy())
            accuracy_count += np.sum(preds == labels.cpu().numpy())

    avg_loss = running_loss / len(dataloader)
    mae = np.mean(np.abs(np.array(all_predictions) - np.array(all_labels)))
    accuracy = accuracy_count / len(dataloader.dataset)

    if mode == 'test' and rank == 0:
        # Save predictions and labels to files
        output_file = f"./test_results_{accuracy:.4f}.csv"
        
        with open(f"{config.output_dir}/{output_file}", 'w', encoding='utf-8') as f:
            f.write("file_name,prediction,label\n")
            for fname, pred, label in zip(all_source_files, all_predictions, all_labels):
                f.write(f"{fname},{round(pred)},{label}\n")
        print(f"Test results saved to {output_file}")

    return avg_loss, mae, accuracy

def main_worker(rank, world_size, config):
    set_seed(42)

    print(f"Running DDP on rank {rank}.")
    setup(rank, world_size)
    
    writer = SummaryWriter(log_dir=os.path.join(config.output_dir, 'runs')) if rank == 0 else None

    tokenizer = AutoTokenizer.from_pretrained(config.model_name, trust_remote_code=True)
    
    if rank == 0:
        print("Master process (rank 0) is loading data...")
    train_samples = load_data_from_pointer_file(config.train_pointer_file, config.data_base_dir)
    valid_samples = load_data_from_pointer_file(config.test_pointer_file, config.data_base_dir)

    train_dataset = AspectDataset(train_samples, tokenizer, config.max_length)
    valid_dataset = AspectDataset(valid_samples, tokenizer, config.max_length)

    if rank == 0:
        print("\n--- Dataset Summary ---")
        print(f"Training samples:   {len(train_dataset)}")
        print(f"Validation samples: {len(valid_dataset)}")
        print("-----------------------\n")
    
    train_sampler = DistributedSampler(train_dataset, num_replicas=world_size, rank=rank)
    
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer, padding=True)
    custom_collator = CustomDataCollator(data_collator=data_collator)
    # Use the sampler in the DataLoader
    train_dataloader = DataLoader(train_dataset, batch_size=config.batch_size, collate_fn=custom_collator, sampler=train_sampler, shuffle=False)
    val_dataloader = DataLoader(valid_dataset, batch_size=config.batch_size, collate_fn=custom_collator)

    # test_dataloader = DataLoader(test_dataset, batch_size=config.batch_size, collate_fn=data_collator)

    device = torch.device(f'cuda:{rank}')
    model = AspectCountModel(config.model_name).to(device)
    

    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
        lora_dropout=0.1,
        bias="none",
    )
    model = get_peft_model(model, peft_config)

    # for param in model.base_model.regressor.parameters():
    #     param.requires_grad = True

    if rank == 0:
        model.print_trainable_parameters()
    
    model = DDP(model, device_ids=[rank])

    

    loss_fn = nn.L1Loss()
    # optimizer = optim.AdamW(filter(lambda p: p.requires_grad, model.parameters()), lr=config.learning_rate)
    optimizer = optim.AdamW(model.parameters(), lr=config.learning_rate)
    
    num_training_steps = config.num_epochs * len(train_dataloader)
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=0, num_training_steps=num_training_steps
    )
    
    if rank == 0:
        print("Starting training...")
    best_val_acc = float('-inf')
    epochs_no_improve = 0
    global_step = 0
    
    for epoch in range(config.num_epochs):
        train_sampler.set_epoch(epoch)
        
        if rank == 0:
            print(f"\n--- Epoch {epoch+1}/{config.num_epochs} ---")
        
        train_loss, global_step = train_epoch(model, train_dataloader, optimizer, scheduler, loss_fn, device, writer, global_step, rank)
        
        if rank == 0:
            print(f"Epoch {epoch+1} Training Loss: {train_loss:.4f}")
            writer.add_scalar('Loss/train_epoch', train_loss, epoch)

            val_loss, val_mae, val_acc = evaluate(model, val_dataloader, loss_fn, device, desc="Evaluating", rank=rank)
            print(f"Epoch {epoch+1} Validation Loss: {val_loss:.4f} | Validation MAE: {val_mae:.4f} | Validation Accuracy: {val_acc:.4f}")
            writer.add_scalar('Loss/validation', val_loss, epoch)
            writer.add_scalar('MAE/validation', val_mae, epoch)
            writer.add_scalar('Accuracy/validation', val_acc, epoch)
            
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                epochs_no_improve = 0
                print(f"Validation Accuracy improved to {val_acc:.4f}! Saving model...")
                os.makedirs(config.output_dir, exist_ok=True)
                unwrapped_model = model.module
    
                unwrapped_model.save_pretrained(config.output_dir)
                
                head_state_dict = unwrapped_model.base_model.regressor.state_dict()
                torch.save(head_state_dict, os.path.join(config.output_dir, "regressor_head.bin"))
                
                tokenizer.save_pretrained(config.output_dir)
                print(f"LoRA adapter and regressor head saved to {config.output_dir}")
            else:
                epochs_no_improve += 1
                print(f"Validation Accuracy did not improve. Patience: {epochs_no_improve}/{config.patience}")

            if epochs_no_improve >= config.patience:
                print(f"Early stopping triggered after {config.patience} epochs with no improvement.")
                break
    
    cleanup()

def run_testing(config):
    """
    Loads a trained model and evaluates it on the test dataset.
    """
    print("--- Running in Test-Only Mode ---")
    device = "cuda:1" if torch.cuda.is_available() else "cpu"
    
    # 1. Load Tokenizer and Test Data
    print(f"Loading tokenizer from: {config.output_dir}")
    tokenizer = AutoTokenizer.from_pretrained(config.output_dir, trust_remote_code=True)
    
    test_samples = load_data_from_pointer_file(config.test_pointer_file, config.data_base_dir)
    test_dataset = AspectDataset(test_samples, tokenizer, config.max_length)
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer, padding=True)
    custom_collator = CustomDataCollator(data_collator=data_collator)

    test_dataloader = DataLoader(test_dataset, batch_size=config.batch_size, collate_fn=custom_collator)
    print(f"\nLoaded {len(test_dataset)} test samples.")
    
    # 2. Initialize Model and Load Weights
    print(f"Initializing model architecture: {config.model_name}")
    base_model = AspectCountModel(config.model_name).to(device)
    # model = AspectCountModel(config.model_name).to(device)

    print(f"Loading LoRA adapter from: {config.output_dir}")
    model = PeftModel.from_pretrained(base_model, config.output_dir)
    head_weights_path = os.path.join(config.output_dir, "regressor_head.bin")
    model.base_model.regressor.load_state_dict(torch.load(head_weights_path))
    model.to(device) 
    model.eval()
    
    
    # 3. Evaluate on Test Set
    loss_fn = nn.L1Loss()
    test_loss, test_mae, test_acc = evaluate(model, test_dataloader, loss_fn, device, desc="Final Testing", mode='test')

    # 4. Print Results
    print("\n--- Test Set Performance ---")
    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test MAE (Mean Absolute Error): {test_mae:.4f}")
    print(f"Test Rounded Accuracy: {test_acc:.4f}") 
    print("----------------------------\n")
    
if __name__ == "__main__":
    # ADDED: Command-line parser to choose between 'train' and 'test' modes
    parser = argparse.ArgumentParser(description="Train or Test the Aspect Count Model.")
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'],
                        help="Set the script to 'train' or 'test' mode.")
    parser.add_argument('--output_dir', type=str, help="Set the output direction")
    args = parser.parse_args()

    config = Config()
    config.output_dir = f"./trained_aspect_regression/{args.output_dir}"

    if args.mode == 'train':
        # main_worker(1, 1, config)
        world_size = torch.cuda.device_count()
        if world_size > 1:
            print(f"Found {world_size} GPUs, starting DDP training.")
            mp.spawn(main_worker,
                     args=(world_size, config),
                     nprocs=world_size,
                     join=True)
        else:
            print("Found 1 or 0 GPUs, running on single device.")
            # rank 0, world_size 1 for single device run
            main_worker(0, 1, config)
    
    elif args.mode == 'test':
        run_testing(config)

    