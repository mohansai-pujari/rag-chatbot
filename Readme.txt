RAG Chatbot: Ask Your Docs!

A Streamlit-based Retrieval-Augmented Generation (RAG) chatbot to interact with text based documents and web content using an LLM backend.

-----Setup Instructions:---------------------------------------------------------------------------
    - Clone the repository:
        - git clone https://github.com/mohansai-pujari/rag-chatbot.git && cd rag-chatbot
    - Run the setup script:
        - ./setup.sh
    - Add your API key in the config.properties file before running the application:
        - GEMINI_API_KEY=your_api_key_here
    - Run the Streamlit app:
        - streamlit run main.py

-----Docker Support:-------------------------------------------------------------------------------
    - Build the Docker image:
        - docker build -t rag-chatbot .
    - Run the Docker container:
        - docker run -p 8501:8501 rag-chatbot

-----Project Summary:------------------------------------------------------------------------------
    - Upload PDF, DOC, DOCX files.
    - Extract and optionally scrape links from documents.
    - Choose to use sample or custom web links.
    - Documents and scraped content are chunked and indexed.
    - Ask questions to get LLM-powered answers from combined knowledge.

-----Configuration Overview:-----------------------------------------------------------------------
    - The application reads key configurations from the utils/config.py file, including:
        - TOP_K: Number of top documents to retrieve.
        - CHUNK_SIZE, CHUNK_OVERLAP: For text chunking.
        - SAMPLE_ANGEL_ONE_WEB_LINKS: Optional sample URLs to scrape.
        - MODEL_NAME, GEMINI_API_KEY: LLM and credentials.
    - Important: You must add your own GEMINI_API_KEY before launching the application.

-----Maintainer:-----------------------------------------------------------------------------------
Mohan Sai Pujari
Software Development Engineer