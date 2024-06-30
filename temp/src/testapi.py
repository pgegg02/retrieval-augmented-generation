from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('PINECONE_API_KEY')

pc = Pinecone(api_key=api_key)
index = pc.Index("jane-austen")

vec1 = []
for i in range(0,384):
  vec1.append(float(i))

a = index.query(
    namespace="ns1",
    vector=vec1,
    top_k=2,
    include_values=True,
    include_metadata=True,
    filter={"genre": {"$eq": "action"}}
)

print(a)