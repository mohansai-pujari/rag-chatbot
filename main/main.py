import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

import streamlit as st
st.set_page_config(page_title="RAG Chatbot")

from langchain.schema import Document

from llm.model import LLMModel
from llm.prompt import PromptBuilder
from processor.text_processor import TextProcessor
from reader.file_loader import FileLoader
from storage.vector_store import VectorStore
from utils.config import TOP_K, CHUNK_SIZE, CHUNK_OVERLAP, GEMINI_API_KEY, MODEL_NAME, SAMPLE_ANGEL_ONE_WEB_LINKS
from utils.web_scraper import WebScraper
import sys
import asyncio



try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

if sys.version_info >= (3, 13):
    st.warning("Python 3.13 is not fully supported. Please downgrade to Python 3.10 or 3.11 for full compatibility.")

def main():
    # st.set_page_config(page_title="RAG Chatbot")
    st.title("RAG Chatbot: Ask Your Docs!")

    uploaded_files = st.file_uploader(
        "Upload PDF/DOC/DOCX files",
        accept_multiple_files=True,
        type=["pdf", "doc", "docx"]
    )

    # Initialize session state
    if "all_docs" not in st.session_state:
        st.session_state.all_docs = []
    if "all_links" not in st.session_state:
        st.session_state.all_links = set()
    if "file_processed" not in st.session_state:
        st.session_state.file_processed = False
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    if "llm" not in st.session_state:
        st.session_state.llm = None
    if "chunks" not in st.session_state:
        st.session_state.chunks = None
    if "proceed_links" not in st.session_state:
        st.session_state.proceed_links = False

    if uploaded_files and not st.session_state.file_processed:
        st.info("Loading files and extracting links...")

        all_docs = []
        all_links = set()

        for file in uploaded_files:
            docs, links = FileLoader.load_file(file)
            all_docs.extend(docs)
            all_links.update(links)

        link_option = st.radio(
            "How would you like to include web links?",
            ("Don't use any links", "Use sample AngleOne links", "Enter custom links"),
            index=0,
            key="link_choice"
        )

        if link_option == "Use sample AngleOne links":
            if st.button("Use Sample AngleOne Links"):
                urls = [url.strip() for url in SAMPLE_ANGEL_ONE_WEB_LINKS.split(",")]
                all_links.update(urls)
                st.session_state.proceed_links = True

        elif link_option == "Enter custom links":
            custom_input = st.text_input("Enter URLs separated by commas:")
            if st.button("Submit Custom Links") and custom_input:
                urls = [url.strip() for url in custom_input.split(",") if url.strip()]
                all_links.update(urls)
                st.session_state.proceed_links = True

        elif link_option == "Don't use any links":
            if st.button("Proceed without Links"):
                st.session_state.proceed_links = True

        if st.session_state.proceed_links:
            if all_links:
                st.info("Scraping webpage data...")
                processed_links = set()
                for url in list(all_links):
                    if url in processed_links:
                        continue
                    processed_links.add(url)
                    scraped_text, new_links = WebScraper.scrape_text_and_links(url)
                    if scraped_text:
                        all_docs.append(Document(page_content=scraped_text, metadata={"source": url}))
                    all_links.update(set(new_links) - processed_links)

            st.session_state.all_docs = all_docs
            st.session_state.all_links = all_links
            st.session_state.file_processed = True

    all_docs = st.session_state.all_docs
    if all_docs and not st.session_state.chunks:
        st.info("Processing documents and webpages...")

        with st.spinner("Splitting documents..."):
            chunks = TextProcessor.split_documents(all_docs, CHUNK_SIZE, CHUNK_OVERLAP)
            st.session_state.chunks = chunks

        with st.spinner("Creating vector store..."):
            store = VectorStore()
            store.create_store(chunks)
            st.session_state.vector_store = store

        with st.spinner("Initializing LLM model..."):
            llm = LLMModel(gemini_api_key=GEMINI_API_KEY, model_name=MODEL_NAME)
            st.session_state.llm = llm

    if st.session_state.vector_store and st.session_state.llm:
        question = st.text_input("Ask a question:")
        if question:
            results = st.session_state.vector_store.search(question, TOP_K)
            context = "\n\n".join([doc.page_content for doc in results])
            prompt = PromptBuilder.build_prompt(context, question)
            response = st.session_state.llm.get_response(prompt)
            st.write("### Answer:")
            st.write(response)

if __name__ == "__main__":
    main()
