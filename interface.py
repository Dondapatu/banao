from model_loader import load_model
from chat_memory import ChatMemory
import torch

def main():
    tokenizer, model = load_model()
    memory = ChatMemory()

    print("Bot: Hello! Ask me anything. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Bot: Goodbye!")
            break

        prompt = memory.build_prompt(user_input)
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
        memory.add_turn(user_input, bot_reply)


if __name__ == "__main__":
    main()