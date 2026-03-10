import os

def validate_file(file_path):
    if not os.path.exists(file_path):
        raise Exception("File not found")

    if not file_path.endswith((".pdf",".docx")):
        raise Exception("Unsupported format")

    return True