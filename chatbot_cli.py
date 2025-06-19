from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load medium factual model (Flan-T5)
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Chat memory (last 5 exchanges)
chat_history = []

print("Bot: Hello! I’m your chatbot. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.strip().lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Build prompt with simple memory
    context = ""
    for past in chat_history[-5:]:
        context += f"User: {past['user']}\nBot: {past['bot']}\n"
    context += f"User: {user_input}\nBot:"

    # Tokenize and generate
    inputs = tokenizer(context, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print(f"Bot: {response}\n")

    # Save to history
    chat_history.append({"user": user_input, "bot": response})
