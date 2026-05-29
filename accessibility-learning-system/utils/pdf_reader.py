import PyPDF2


def extract_text_from_pdf(pdf_source):
    """Extract all text content from a PDF file path or file-like stream."""
    text = []
    if isinstance(pdf_source, str):
        with open(pdf_source, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
    else:
        reader = PyPDF2.PdfReader(pdf_source)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)
