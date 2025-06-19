# CLI Chatbot with Memory (Offline, Lightweight)

This project is a simple, offline-capable chatbot that runs in your terminal using Hugging Face's TinyLlama model. It supports basic natural language responses and maintains short-term memory of the conversation to offer contextual replies.

## Features

* Command Line Interface (CLI) based chatbot
* Lightweight: uses TinyLlama-1.1B-Chat model (\~1GB)
* No API key required
* Chat memory: remembers last 5 user-bot interactions
* Modular codebase for readability and easy extension

## File Structure

* `model_loader.py` – Handles loading the tokenizer and language model
* `chat_memory.py` – Manages a buffer that stores the last few user-bot messages
* `interface.py` – Main loop for chatting via CLI

## Setup Instructions

### 1. Install Required Libraries

Make sure you have Python 3.8+ and run:

```
pip install transformers accelerate sentencepiece
```

### 2. Run the Chatbot

Navigate to the folder where your code is saved and run:

```
python interface.py
```

## Example Interaction

```
Bot: Hello! Ask me anything. Type 'exit' to quit.

You: What is the capital of France?
Bot: The capital of France is Paris.

You: And Germany?
Bot: The capital of Germany is Berlin.

You: exit
Bot: Goodbye!
```

## How It Works

* The chatbot builds a prompt that includes a few previous exchanges.
* This prompt is passed to the TinyLlama model to generate context-aware responses.
* The output is printed in the terminal, simulating a real-time chat experience.

## Design Notes

* The chat memory is limited to 5 exchanges for performance and clarity.
* The project is fully modular: each component (model, memory, interface) is in a separate file.
* This project can be extended to include GUI, speech, or logging features.

## Suggestions for Extension

* Add chat logging to a text file
* Implement a basic GUI with Tkinter or a web frontend
* Integrate text-to-speech (TTS) for voice-based replies

## Final Notes

This project serves as a great starting point for learning how to integrate transformer models into real applications. You can run it entirely offline after the initial model download, making it ideal for local experimentation and learning.
