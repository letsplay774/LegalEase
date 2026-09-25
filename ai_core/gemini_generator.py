import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file explicitly from project root
root_dir = Path(__file__).resolve().parent.parent
env_path = root_dir / ".env"
load_dotenv(dotenv_path=env_path)

class GeminiDocumentGenerator:
    def __init__(self, model_name: str = "gemini-3.6-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(f"GEMINI_API_KEY not found in .env file at {env_path}")
        
        genai.configure(api_key=api_key.strip())
        self.model = genai.GenerativeModel(model_name)

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        prompt = (
            f"Generate a comprehensive, formal, and professionally structured legal document titled '{document_type}'.\n\n"
            f"Involved Parties:\n{parties}\n\n"
            f"Effective Date:\n{dates}\n\n"
            f"Terms and Conditions:\n{terms}\n\n"
            "Ensure formal legal structure with clear sections and clauses."
        )
        response = self.model.generate_content(prompt)
        return response.text