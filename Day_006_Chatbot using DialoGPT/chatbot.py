from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")  # use medium for better responses
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None
print("AI ChatBot: Type 'exit' to end chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    attention_mask = torch.ones_like(input_ids)  # 👈 FIX here

    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
        attention_mask = torch.ones_like(bot_input_ids)  # for full sequence
    else:
        bot_input_ids = input_ids

    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        attention_mask=attention_mask,  # 👈 pass attention mask
        no_repeat_ngram_size=3,         # 👈 reduce repetitive output
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8
    )

    reply = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"Bot: {reply}\n")
