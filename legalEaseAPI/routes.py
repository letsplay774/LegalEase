from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()

# Initialize the Gemini document generator instance
try:
    gemini_generator = GeminiDocumentGenerator()
except Exception as e:
    gemini_generator = None
    print(f"Warning: GeminiDocumentGenerator failed to initialize. Check GEMINI_API_KEY. Error: {e}")

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    if not gemini_generator:
        raise HTTPException(status_code=500, detail="Gemini API is not properly configured.")
    
    try:
        response = gemini_generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            dates=request.dates
        )
        return {"document": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))