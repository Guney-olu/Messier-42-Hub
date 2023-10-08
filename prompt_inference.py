from transformers import AutoTokenizer
import transformers
import torch

model = "AryanNsc/7bfinetunetest1"


tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
)

input_prompt = input("Enter the type of projects you want to learn about: ")
prompt= f"List only the key skills required in this prompt: {input_prompt}"
sequences = pipeline(
    f'[INST] {prompt} [/INST]',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=400,
)


for seq in sequences:
    print(f"Result: {seq['generated_text']}")