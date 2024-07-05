import openai
import os
from dotenv import load_dotenv


def get_answer_to_question(question, retrieved_context):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question},
                  {"role": "system", "content": f"You are a RAG System that gets a Users Question,"
                                                f"plus provided context that has been retrieved from"
                                                f"a vector database, answer the question to the best "
                                                f"of your abilities using the provided context and the"
                                                f"question. Here is the provided context: {retrieved_context}"}],
    )
    return response['choices'][0]['message']['content']

