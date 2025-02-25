from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = "./mistral-orientation"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", torch_dtype=torch.float16)

# Tester une question
input_text = "Je ne sais pas quoi faire après le bac."
inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

output = model.generate(**inputs, max_length=300, temperature=0.7, top_p=0.9, do_sample=True)
print(tokenizer.decode(output[0], skip_special_tokens=True))
