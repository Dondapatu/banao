from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,   # safer for CPU
    device_map="auto"            # works with CPU or GPU
)

chat_history = []

print("Bot: Hello! Ask me anything. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Build prompt with memory
    prompt = ""
    for turn in chat_history[-5:]:
        prompt += f"<|user|>\n{turn['user']}\n<|assistant|>\n{turn['bot']}\n"
    prompt += f"<|user|>\n{user_input}\n<|assistant|>\n"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.7,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    bot_reply = full_output.split("<|assistant|>")[-1].strip()

    print(f"Bot: {bot_reply}\n")
    chat_history.append({"user": user_input, "bot": bot_reply})
