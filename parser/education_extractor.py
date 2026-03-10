def extract_education(text):

    education_keywords = [
        "B.Tech", "Bachelor", "BSc", "B.E",
        "M.Tech", "Master", "MSc", "PhD",
        "MBA", "BCA", "MCA"
    ]

    education_found = []

    for edu in education_keywords:
        if edu.lower() in text.lower():
            education_found.append(edu)

    return list(set(education_found))