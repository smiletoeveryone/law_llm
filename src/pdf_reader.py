from PyPDF2 import PdfReader
import os

def read_pdfs_from_folder(folder_path):
    text = ""
    for file in os.listdir(folder_path):
        if file.endswith('.pdf'):
            reader = PdfReader(os.path.join(folder_path, file))
            for page in reader.pages:
                text += page.extract_text()
    return text
