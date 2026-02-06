from .resume_utils import extract_text
from matching.embedding_model import model

def generate_resume_vector(profile):
    # Safety check
    if not profile.resume_file:
        return

    # Correct field name
    resume_path = profile.resume_file.path

    # Extract text
    resume_text = extract_text(resume_path)

    if not resume_text.strip():
        return

    # Generate embedding
    vector = model.encode(resume_text).tolist()

    # Save vector
    profile.resume_vector = vector
    profile.save()
