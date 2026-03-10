def build_profile(ner, contact, skills, education):

    profile = {

        "name": ner["name"],

        "email": contact["email"],

        "phone": contact["phone"],

        "linkedin": contact["linkedin"],

        "github": contact["github"],

        "skills": skills,

        "education": education,

        "organizations": ner["organizations"],

        "locations": ner["locations"]

    }

    return profile