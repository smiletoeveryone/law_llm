from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(text):
    sentences = text.split('.')
    embeddings = model.encode(sentences)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, sentences

def search_similar(query, index, sentences, k=5):
    query_emb = model.encode([query])
    distances, indices = index.search(query_emb, k)
    results = [sentences[i] for i in indices[0]]
    return results
