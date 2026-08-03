import os
import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from ocr import extract_text_from_pdf
from llm import analyze_document


app = FastAPI(
    title="OCR Document AI",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "OCR Document AI Backend Running"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    pdf_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(pdf_path)

    analysis = analyze_document(extracted_text)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "analysis": analysis
    }