import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os

def analyze_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    try:
        # Handle image files
        if ext in ['.jpg', '.jpeg', '.png']:
            image = Image.open(filepath)
            text = pytesseract.image_to_string(image)
            summary = text.strip()[:300] if text else "No readable text found in image."
            return {'summary': summary, 'type': 'image'}

        # Handle PDF files
        elif ext == '.pdf':
            doc = fitz.open(filepath)
            text = ""
            for page in doc:
                text += page.get_text()
            summary = text.strip()[:300] if text else "No readable text found in PDF."
            return {'summary': summary, 'type': 'pdf'}

        # Handle plain text files
        elif ext == '.txt':
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            summary = text.strip()[:300] if text else "Text file is empty."
            return {'summary': summary, 'type': 'text'}

        # Unsupported file type
        else:
            return {'summary': 'Unsupported file type.', 'type': 'unsupported'}

    except Exception as e:
        return {'summary': f'Error processing file: {str(e)}', 'type': 'error'}
