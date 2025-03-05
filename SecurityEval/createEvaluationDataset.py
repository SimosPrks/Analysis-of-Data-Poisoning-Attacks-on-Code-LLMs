import json
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from config import SALLM_DATA_PATH, GENERATED_CODE_OUTPUT_PATH, MODEL_PATH, MODIFIED_MODEL_PATH


# Use MODIFIED_MODEL_PATH or MODEL_PATH 
model_path = MODIFIED_MODEL_PATH
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", torch_dtype=torch.float16)


# File paths
input_path = SALLM_DATA_PATH
output_path = GENERATED_CODE_OUTPUT_PATH

# Result list
results = []

# Load prompts from JSONL
with open(input_path, "r") as file:
    for line in file:
        data = json.loads(line)
        prompt = data["prompt"]  # Direct prompt from the JSONL file

        # Generate code
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

        with torch.no_grad():
            outputs = model.generate(
            inputs.input_ids,
            max_new_tokens=128,
            temperature=0.2,
            top_p=0.95,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
            repetition_penalty=1.1  # Slight penalty for repetitions
)


        # Extract generated code
        generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Save data
        data["Generated_code"] = generated_code
        results.append(data)

        # Show progress
        print(f"Processed: {data['id']}")

# Save results in JSONL format
with open(output_path, "w") as outfile:
    for result in results:
        outfile.write(json.dumps(result) + "\n")

print(f"Generated results saved in {output_path}.")
