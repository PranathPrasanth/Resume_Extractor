skills_list = [
    "Python","Java","C","C++","SQL",
    "Machine Learning","Deep Learning",
    "Data Science","NLP","React",
    "HTML","CSS","JavaScript",
    "TensorFlow","PyTorch",
    "Django","Flask","Node.js"
]

def extract_skills(text):

    skills_found = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            skills_found.append(skill)

    return list(set(skills_found))