EXP_KEYWORDS = ["experience", "worked", "company", "intern", "engineer"]

def extract_experience(text):
    lines = text.lower().split("\n")
    experience = []

    for line in lines:
        for keyword in EXP_KEYWORDS:
            if keyword in line:
                experience.append(line.strip())

    return experience[:5]
