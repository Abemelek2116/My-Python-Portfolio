# jobs/services.py
from sentence_transformers import SentenceTransformer
from .models import Job

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_job_vector(job):
    """
    Generate and store embedding for a job
    """
    # Combine job info into ONE string
    text = f"{job.title} {job.description}"

    # Optional: include skills if they exist
    skills = job.required_skills.all()
    if skills.exists():
        skill_text = " ".join([skill.name for skill in skills])
        text += " " + skill_text

    # Generate vector
    vector = model.encode(text)

    # Save to DB
    job.job_vector = vector.tolist()
    job.save()
