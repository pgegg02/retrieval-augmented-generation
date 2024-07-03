from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import os
from dotenv import load_dotenv

sentences = ['whats the story about titled "The Adventures of Aiden and the Enchanted Forest" about']

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

query_vector = embeddings[0].tolist()
#print(type(query_vector))
#print(query_vector)

load_dotenv()
pine_cone_api_key = os.getenv('PINECONE_API_KEY')

pc = Pinecone(api_key=pine_cone_api_key)
index = pc.Index("gpt-story")
print(index.query(
    namespace="sentences",
    vector=[query_vector],
    top_k=1,
    include_values=True,
    include_metadata=True
))