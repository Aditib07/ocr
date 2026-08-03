import os
from dotenv import load_dotenv
import easyocr
from pdf2image import convert_from_path

# Load environment variables
load_dotenv()

POPPLER_PATH = os.getenv("POPPLER_PATH")

# Initialize EasyOCR only once
reader = easyocr.Reader(["en"])


def extract_text_from_pdf(pdf_path):
    image_folder = "uploads/images"
    os.makedirs(image_folder, exist_ok=True)

    # Convert PDF pages to images
    if POPPLER_PATH:
        pages = convert_from_path(
            pdf_path,
            poppler_path=POPPLER_PATH
        )
    else:
        pages = convert_from_path(pdf_path)

    extracted_pages = []

    for page_number, page in enumerate(pages, start=1):
        image_path = os.path.join(
            image_folder,
            f"page_{page_number}.png"
        )

        page.save(image_path, "PNG")

        results = reader.readtext(
            image_path,
            detail=0,
            paragraph=True
        )

        page_text = "\n".join(results)
        extracted_pages.append(page_text)

    return "\n\n".join(extracted_pages)