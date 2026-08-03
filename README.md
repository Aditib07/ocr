# OCR Document AI

An AI-powered document analyzer that extracts text from PDF documents using OCR and generates intelligent summaries and key information using Google's Gemini API.

## Features

- PDF text extraction using EasyOCR
- AI-powered document analysis
- Document type detection
- Automatic summary generation
- Key information extraction
- React frontend with FastAPI backend

## Tech Stack

### Frontend
- React (Vite)

### Backend
- FastAPI
- Python

### AI
- Google Gemini API

### OCR
- EasyOCR
- pdf2image

## Installation

### Backend

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

### Frontend

```bash
npm install
npm run dev
```

## Project Structure

```
OCR_Document_AI/
│
├── backend/
├── frontend/
└── README.md
```

## Author

Arnav
