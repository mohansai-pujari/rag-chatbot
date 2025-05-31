import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader
import fitz
import docx
import re

class FileLoader:
    @staticmethod
    def load_file(uploaded_file):
        ext = os.path.splitext(uploaded_file.name)[1].lower()
        links = set()

        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        if ext == ".pdf":
            loader = PyPDFLoader(tmp_path)
            docs = loader.load()
            links.update(FileLoader._extract_links_from_pdf(tmp_path))

        elif ext in [".doc", ".docx"]:
            loader = UnstructuredWordDocumentLoader(tmp_path)
            docs = loader.load()
            links.update(FileLoader._extract_links_from_docx(tmp_path))

        else:
            raise ValueError(f"Unsupported file format: {ext}")

        return docs, links

    @staticmethod
    def _extract_links_from_pdf(pdf_path):
        links = set()
        try:
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    for link in page.get_links():
                        uri = link.get("uri")
                        if uri and uri.startswith("http"):
                            links.add(uri)
        except Exception as e:
            print(f"Error extracting PDF links: {e}")
        return links

    @staticmethod
    def _extract_links_from_docx(docx_path):
        links = set()
        try:
            document = docx.Document(docx_path)
            for para in document.paragraphs:
                hyperlink_matches = re.findall(r'(https?://\S+)', para.text)
                links.update(hyperlink_matches)
        except Exception as e:
            print(f"Error extracting DOCX links: {e}")
        return links
