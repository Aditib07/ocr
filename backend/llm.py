import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_document(text):

    prompt = f"""
You are an AI Document Analyzer.

Analyze the following document carefully.

Return ONLY valid JSON.

Format:

{{
    "document_type": "",
    "summary": "",
    "key_points": [],
    "important_information": {{}}
}}

Rules:

1. Identify the document type.
2. Write a short summary (3-5 lines).
3. Extract important key points.
4. Extract important information as key-value pairs.
5. If a field is missing, return an empty string.
6. Do not return markdown.
7. Do not explain anything outside the JSON.

Document:

{text}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    output = response.text.strip()

    if output.startswith("```json"):
        output = output.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(output)
    except Exception:
        return {
            "document_type": "Unknown",
            "summary": output,
            "key_points": [],
            "important_information": {}
        }