import openai
import os
from dotenv import load_dotenv

def get_answer_to_question(question):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']

'''question = "What is the capital of France?"
answer = get_answer_to_question(question)
print(answer)'''

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
print(HF_TOKEN)