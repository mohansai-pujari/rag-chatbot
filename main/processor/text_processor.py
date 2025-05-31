from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextProcessor:
    @staticmethod
    def split_documents(docs, chunk_size, chunk_overlap):
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return splitter.split_documents(docs)
