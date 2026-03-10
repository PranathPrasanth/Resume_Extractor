import json

from parser.file_validator import validate_file
from parser.text_extractor import extract_text
from parser.ner_extractor import extract_entities
from parser.regex_extractor import extract_contact
from parser.profile_builder import build_profile
from parser.skills_extractor import extract_skills
from parser.education_extractor import extract_education

resume_path = "resume_samples/Resume.pdf"

validate_file(resume_path)

text = extract_text(resume_path)

ner_data = extract_entities(text)

contact_data = extract_contact(text)

skills = extract_skills(text)

# ADD THIS LINE
education = extract_education(text)

profile = build_profile(ner_data, contact_data, skills, education)

print(profile)

with open("data/candidate_profile.json","w") as f:
    json.dump(profile,f,indent=4)