from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


def index_docs(MODEL, docs):
    embeddings = OllamaEmbeddings(model=MODEL)
    ids = InMemoryVectorStore(embeddings)
    ids.add_documents(documents=docs)
    return ids
