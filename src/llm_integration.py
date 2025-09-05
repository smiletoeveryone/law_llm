from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings

llm = OllamaLLM(model="llama2")

def chat_with_llm(query, docs):
    # For simplicity, just call LLM with query and docs
    context = " ".join(docs)
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = llm(prompt)
    return response
