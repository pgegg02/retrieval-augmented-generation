from sentence_transformers import SentenceTransformer

sentences = ['whats the story about titled "The Adventures of Aiden and the Enchanted Forest" about']

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
