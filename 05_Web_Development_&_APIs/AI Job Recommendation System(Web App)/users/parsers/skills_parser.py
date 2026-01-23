SKILLS_LIST = [
    "python", "django", "sql", "javascript",
    "html", "css", "react", "git",
    "machine learning", "nlp", "docker"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_LIST:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
