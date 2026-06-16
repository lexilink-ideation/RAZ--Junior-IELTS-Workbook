#!/usr/bin/env python3
"""
RAZ Book PDF Extractor
Extracts text from a RAZ reader PDF and prints it to stdout.
Usage: python3 extract_pdf.py <path_to_pdf>
"""
import sys
import json

def extract(pdf_path):
    try:
        import pdfplumber
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfplumber", "--break-system-packages", "-q"])
        import pdfplumber

    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages.append({"page": i + 1, "text": text.strip()})

    full_text = "\n\n--- PAGE BREAK ---\n\n".join(p["text"] for p in pages)
    result = {
        "total_pages": len(pages),
        "full_text": full_text,
        "pages": pages
    }
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No PDF path provided"}))
        sys.exit(1)
    extract(sys.argv[1])
