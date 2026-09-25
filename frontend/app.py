import sys
import os
import requests
import streamlit as st

# Ensure root directory is accessible for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_core.generator import sanitize_text, format_html_preview, format_docx, format_pdf

# Page Configuration
st.set_page_config(page_title="LegalEase", layout="centered", page_icon="⚖️")

# Header & Logo Display
logo_path = os.path.join(os.path.dirname(__file__), "..", "Image", "Logo.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown("<h1 style='text-align: center;'>⚖️ LegalEase</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

# User Input Form
st.subheader("Document Details")
document_type = st.text_input("Document Type (Ex. Agreement, Contract, NDA)", placeholder="e.g., Freelance Work Contract")
parties = st.text_area("Parties Involved", placeholder="e.g., Jane Doe (Service Provider), TechNova Inc. (Client)")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)", placeholder="e.g., Work must be delivered by May 15, 2025; Payment within 7 days of invoice;")
dates = st.text_input("Effective Date", placeholder="e.g., April 15, 2025")

# Session State Initializations
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "show_edit" not in st.session_state:
    st.session_state.show_edit = False

# Action Button
if st.button("Generate Document"):
    if not document_type or not parties or not terms or not dates:
        st.warning("Please fill in all input fields before generating.")
    else:
        with st.spinner("Generating document via Gemini API..."):
            try:
                payload = {
                    "document_type": document_type,
                    "parties": parties,
                    "terms": terms,
                    "dates": dates
                }
                # Send POST request to FastAPI backend
                response = requests.post("http://127.0.0.1:8000/generate", json=payload)
                
                if response.status_code == 200:
                    raw_doc = response.json().get("document", "")
                    st.session_state.generated_text = sanitize_text(raw_doc)
                    st.session_state.show_edit = False
                    st.success("Document Generated Successfully!")
                else:
                    st.error(f"API Error: {response.json().get('detail', 'Failed to generate')}")
            except Exception as e:
                st.error(f"Backend Connection Error: {e}. Make sure FastAPI server is running on port 8000.")

# Output / Edit / Download Section
if st.session_state.generated_text:
    st.markdown("---")
    st.subheader("Generated Document Preview")

    # Dark-themed Scrollable HTML Preview
    styled_html = format_html_preview(st.session_state.generated_text)
    st.markdown(
        f"<div style='background-color: #1e1e1e; padding: 20px; border-radius: 8px; color: #e0e0e0; max-height: 380px; overflow-y: auto;'>{styled_html}</div>",
        unsafe_allow_html=True
    )

    st.write("")
    if st.button("✏️ Click to Edit Document"):
        st.session_state.show_edit = not st.session_state.show_edit

    # Inline Editor
    if st.session_state.show_edit:
        edited_text = st.text_area("Edit Document Below:", value=st.session_state.generated_text, height=300)
        st.session_state.generated_text = edited_text

    st.markdown("### Download Options")
    col_txt, col_docx, col_pdf = st.columns(3)
    file_stem = document_type.lower().replace(" ", "_") if document_type else "legal_document"

    with col_txt:
        st.download_button(
            label="📄 Download as .TXT",
            data=st.session_state.generated_text,
            file_name=f"{file_stem}.txt",
            mime="text/plain"
        )

    with col_docx:
        docx_bytes = format_docx(st.session_state.generated_text, document_type or "Legal Document")
        st.download_button(
            label="📝 Download as .DOCX",
            data=docx_bytes,
            file_name=f"{file_stem}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    with col_pdf:
        pdf_bytes = format_pdf(st.session_state.generated_text, document_type or "Legal Document")
        st.download_button(
            label="📕 Download as .PDF",
            data=pdf_bytes,
            file_name=f"{file_stem}.pdf",
            mime="application/pdf"
        )