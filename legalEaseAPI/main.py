import sys
import os

# Ensure the root project directory is in Python path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from legalEaseAPI.routes import router

app = FastAPI(title="LegalEase AI Legal Document Generator")

# Include API routes from routes.py
app.include_router(router)

# Health check root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to LegalEase AI Legal Document Generator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("legalEaseAPI.main:app", host="127.0.0.1", port=8000, reload=True)