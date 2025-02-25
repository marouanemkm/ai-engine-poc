from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "mistralai/Mistral-7B-Instruct-v0.1"


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", torch_dtype=torch.float16
)

model = torch.compile(model)


input_text = "Question : Comment puis-je m'orienter après le bac ?\nRéponse détaillée :"

inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

output = model.generate(
    **inputs,
    max_length=200,   
    temperature=0.9,  
    top_p=0.95,       
    do_sample=True
)

print(tokenizer.decode(output[0], skip_special_tokens=True))
