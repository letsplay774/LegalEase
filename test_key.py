import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=key.strip())

# List available models for your key
print("--- AVAILABLE MODELS FOR YOUR KEY ---")
available_models = []
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        # Strip the 'models/' prefix for clean usage
        model_name = m.name.replace("models/", "")
        available_models.append(model_name)
        print(f"  • {model_name}")

if available_models:
    selected_model = available_models[0]
    print(f"\nTesting with model: {selected_model}...")
    model = genai.GenerativeModel(selected_model)
    response = model.generate_content("Hello! Confirm API working.")
    print(f"✅ SUCCESS using '{selected_model}':", response.text.strip())