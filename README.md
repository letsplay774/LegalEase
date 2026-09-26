
# LegalEase — Project Report & Documentation

## 1. Abstract
**LegalEase** is an end-to-end, artificial intelligence-powered legal document generation platform designed to automate the drafting of standard contracts, non-disclosure agreements (NDAs), and legal notices. Built using a modular micro-architecture with **FastAPI** for backend API management, **Streamlit** for an interactive user interface, and Google's **Gemini 1.5 Pro** model for natural language processing and document drafting, the platform enables users to generate tailored legal documents within seconds in `.txt`, `.docx`, and `.pdf` formats.

---

## 2. System Architecture

```text
[ Streamlit UI ]  <--->  [ FastAPI REST Server ]  <--->  [ Gemini 1.5 Pro LLM ]
   (Frontend)                     (Backend)                    (AI Core)

 * Frontend (Streamlit): Interface for user input collection (document type, party details, key clauses, dates).
 * Backend (FastAPI): High-performance REST API handling validation, request routing, and file exports.
 * AI Engine (Gemini 1.5 Pro): Ingests structured prompt templates and outputs professional legal text.
3. Technology Stack
| Component | Technology | Role |
|---|---|---|
| Language | Python 3.10+ | Core Application Programming |
| Backend Framework | FastAPI + Uvicorn | RESTful Web Services & Middleware |
| Frontend Framework | Streamlit | Web Interface & User Interaction |
| AI Model | Google Gemini 1.5 Pro | Automated Legal Text Generation |
| Document Export | python-docx & FPDF | Formatting and exporting .docx and .pdf files |
| Environment | python-dotenv | Secure API Key Management |
4. Repository Directory Structure
LegalEase/
│
├── ai_core/
│   └── gemini_generator.py     # Prompt engineering & Gemini API logic
├── legalEaseAPI/
│   ├── main.py                 # FastAPI application setup
│   └── routes.py               # REST API endpoints
├── frontend/
│   └── app.py                  # Streamlit frontend layout
├── .env.example                # Sample environment template
├── requirements.txt            # Python dependencies
├── README.md                   # Main GitHub Landing Page
└── DOCUMENTATION.md            # Detailed Technical Project Report

5. Execution & Setup Instructions
1. Virtual Environment Setup
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Configure API Key
Create a .env file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here

4. Run the Project
Open two separate terminal windows:
 * Terminal 1 (Backend API):
   uvicorn legalEaseAPI.main:app --reload

 * Terminal 2 (Frontend Interface):
   streamlit run frontend/app.py

6. Future Enhancements
 * User Authentication: Role-based access using JWT tokens.
 * Database Storage: Database integration (PostgreSQL/SQLite) for saved contracts.
 * Digital Signatures: Integrated PDF e-signature functionality.

---
