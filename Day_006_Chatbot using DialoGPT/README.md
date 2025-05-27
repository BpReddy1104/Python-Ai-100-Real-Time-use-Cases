# 🤖Chatbot using DialoGPT (Hugging Face Transformers)

This is a simple terminal-based conversational chatbot built using Microsoft's [DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium) model via the Hugging Face `transformers` library. It simulates human-like conversations and maintains chat history for context-aware responses.

---

## 📦 Features

- Uses DialoGPT-medium for high-quality responses
- Maintains chat history to improve context understanding
- Interactive terminal interface
- Supports natural and diverse replies using sampling techniques

---

## 🧰 Requirements

- Python 3.7+
- PyTorch
- Transformers library (by Hugging Face)

---

## 🛠 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/dialoGPT-chatbot.git
   cd dialoGPT-chatbot
# Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the dependencies:
pip install transformers torch

# 🚀 Running the Chatbot
python chatbot.py