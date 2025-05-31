#!/bin/bash
echo "Setting up project..."

# Create virtual environment if not present
python3 -m venv venv_rag_bot
source venv_rag_bot/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt

# Download required NLTK data
python3 -m nltk.downloader punkt

echo "Setup complete!"
