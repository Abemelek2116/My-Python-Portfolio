# users/resume_utils.py
import docx

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        try:
            import pdfplumber
        except Exception:
            # fallback to PyPDF2 if pdfplumber is not installed
            try:
                from PyPDF2 import PdfReader
            except Exception:
                raise ImportError("Neither pdfplumber nor PyPDF2 is installed; install one to extract PDFs")
            reader = PdfReader(file_path)
            for page in reader.pages:
                text += (page.extract_text() or "")
            return text
        else:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            return text

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    return ""
