import re

def extract_contact(text):

    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    phone = re.findall(r"\+?\d[\d -]{8,12}\d", text)

    linkedin = re.findall(r"linkedin\.com\/[A-Za-z0-9\/\-]+", text)

    github = re.findall(r"github\.com\/[A-Za-z0-9\/\-]+", text)

    return {
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "linkedin": linkedin[0] if linkedin else "",
        "github": github[0] if github else ""
    }