from pinecone import Pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from constants import TEMP
import os
import json


def extract_sentences(jsonfile: str):
    sentences = []
    with open(jsonfile, 'r') as f:
        data = json.load(f)

    for item in data:
        sentences.extend(item.replace("\n", " ").split('. '))
    return sentences


def embedd_text(sentences):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings


def push_embeddings_to_db(embeddings: list):
    load_dotenv()
    pine_cone_api_key = os.getenv('PINECONE_API_KEY')

    pc = Pinecone(api_key=pine_cone_api_key)
    index = pc.Index("gpt-story")

    vectors = []

    for i, embedded_sentence in enumerate(embeddings):
        vectors.append({"id": f"sentence-{i}", "values": embedded_sentence})

    index.upsert(vectors, namespace='sentences')




if __name__ == '__main__':
    json_file = f'{TEMP}/jsons/GPT_Story.json'
    extracted_sentences = extract_sentences(json_file)
    embedding = embedd_text(extracted_sentences)
    push_embeddings_to_db(embedding)