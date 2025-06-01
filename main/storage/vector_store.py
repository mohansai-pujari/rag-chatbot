from langchain_community.vectorstores import FAISS

class VectorStore:
    def __init__(self):
        self.store = None

    def create_store(self, documents):
        from langchain_community.embeddings import HuggingFaceEmbeddings  # lazy import
        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        self.store = FAISS.from_documents(documents, embedding_model)

    def search(self, query, top_k):
        return self.store.similarity_search(query, k=top_k)
