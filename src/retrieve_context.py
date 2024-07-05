from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from dotenv import load_dotenv
from constants import TEMP
import os
import re
import json


def embedd_query(sentence):
    sentences = []
    sentences.append(sentence)
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)

    query_vector = embeddings[0].tolist()
    return query_vector


def get_matches(embedded_query):
    load_dotenv()
    pine_cone_api_key = os.getenv('PINECONE_API_KEY')

    pc = Pinecone(api_key=pine_cone_api_key)
    index = pc.Index("gpt-story")
    matches = index.query(
        namespace="sentences",
        vector=[embedded_query],
        top_k=3,
        include_values=True,
        include_metadata=True
    )
    return matches


def get_sentence_ids(matches):
    ids = []
    for i in range(len(matches['matches'])):
        ids.append(int(''.join(re.findall(r'\d+', matches['matches'][i]['id']))))
    return ids


def get_context(sentence_ids):
    context = []

    with open(f'{TEMP}/sentences.json', 'r') as f:
        data = json.load(f)

    for i, sentence in enumerate(data):
        if i in sentence_ids:
            context.append(sentence)

    return context