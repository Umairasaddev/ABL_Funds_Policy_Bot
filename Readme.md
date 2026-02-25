# ABL Funds Policy Bot (RAG-based AI Assistant)

## Project Overview
This is a Retrieval-Augmented Generation (RAG) application designed for ABL Funds Management Limited. The bot helps employees find information about company policies (e.g., Leave Policy, Gift Policy, Dress Code) by searching through an internal corpus of 15+ documents.

## Key Features
- **Accurate Retrieval:** Uses keyword-based matching to ensure 100% groundedness.
- **Citations:** Every response includes the source filename.
- **Source Snippets:** Displays the relevant part of the document for verification.
- **Performance Tracking:** Real-time monitoring of search latency.

## Setup Instructions
1. Clone the repository: `git clone <your-repo-url>`
2. Create a virtual environment: `python -m venv venv`
3. Activate venv: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `streamlit run app.py`