from .resume_utils import extract_text
from matching.embedding_model import model

def generate_resume_vector(profile):
    resume_path = profile.resume.path
    resume_text = extract_text(resume_path)

    if not resume_text.strip():
        return

    vector = model.encode(resume_text).tolist()  # convert numpy → list

    profile.resume_vector = vector
    profile.save()
