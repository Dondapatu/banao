CLI Chatbot with Hugging Face
A command-line chatbot built with Hugging Face's T5-small model, featuring a sliding window memory for multi-turn conversations.
Setup Instructions

Install Python 3.8 or higher.
Install dependencies:pip install transformers torch


Clone this repository or download the files.

How to Run

Navigate to the project directory.
Run the chatbot:python interface.py


Type your messages and use /exit to quit.

Sample Interaction
You: What is the capital of France?
Bot: Paris
You: And what about Italy?
Bot: Rome
You: /exit
Exiting chatbot. Goodbye!

Design Decisions

Model Choice: Used google/t5-v1_1-small for its medium size, local compatibility, and accuracy in text-to-text tasks like question-answering.
Memory Buffer: Implemented a sliding window (5 turns) with a system prompt to maintain context and encourage factual responses.
Modularity: Split code into model_loader.py (loads pipeline), chat_memory.py (manages history), and interface.py (runs CLI).
Pipeline: Used Hugging Face’s text2text-generation pipeline for versatile and accurate response generation.

Requirements

Python 3.8+
transformers and torch libraries
No GPU required

