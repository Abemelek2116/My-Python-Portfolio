EDU_KEYWORDS = ["bachelor", "master", "degree", "university", "college"]

def extract_education(text):
    lines = text.lower().split("\n")
    education = []

    for line in lines:
        for keyword in EDU_KEYWORDS:
            if keyword in line:
                education.append(line.strip())

    return education[:3]
