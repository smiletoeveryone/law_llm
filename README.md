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

## Demo
A live demo is available at [Streamlit Cloud Link](https://your-app.streamlit.app) (replace with actual link after deployment).

## Deployment
To deploy the app:
1. Sign up for [Streamlit Cloud](https://streamlit.io/cloud).
2. Connect your GitHub repository.
3. Deploy the app from `src/app.py`.
4. Share the public link for the demo.
