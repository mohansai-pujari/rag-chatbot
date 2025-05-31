from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

class VectorStore:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings()
        self.store = None

    def create_store(self, documents):
        self.store = FAISS.from_documents(documents, self.embedding_model)

    def search(self, query, top_k):
        return self.store.similarity_search(query, k=top_k)
