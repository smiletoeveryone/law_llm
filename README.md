# Law LLM Project

This is a Python LLM project for chatting about lawsuits with domain knowledge from PDFs.

## Features
- Read PDFs for embedding domain knowledge
- Integrate with Ollama for LLM callbacks
- Web UI in Traditional Chinese
- Processed in Anaconda environment

## Setup
1. Install Anaconda or Python.
2. Create environment: `conda env create -f environment.yml` or `pip install -r requirements.txt`
3. Install Ollama and pull a model, e.g., `ollama pull llama2`
4. Run the app: `streamlit run src/app.py`

## Usage
Place PDF files in the `pdfs/` folder for domain knowledge embedding. Then, ask questions about lawsuits in the chat interface.
