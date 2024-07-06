# PDF Query System

This project demonstrates a pipeline for embedding and querying PDF's.
The primary components are:

1. **Embedding**: Transforming the generated story sentences into embeddings using
	https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
1. **Vector Database**: Storing these embeddings in a Pinecone vector database for efficient similarity search.
2. **Query System**: Implementing an API backend that uses OpenAI to process user queries, embedding them, and retrieving relevant story contexts from the vector database.

### Prerequisites

- python ^3.12  
- pypdf2 3.0.1  
- nltk 3.8.1  
- pinecone 4.0.0  
- pinecone-client 4.1.1  
- python-dotenv 1.0.1  
- openai 0.28  
- sentence-transformers 3.0.1
