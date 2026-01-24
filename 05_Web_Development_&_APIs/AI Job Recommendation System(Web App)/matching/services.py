from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from users.models import ParsedResume
from jobs.models import Job
from .utils import normalize_skills

def compute_similarity(resume_vector, job_vector):
    """
    Compute cosine similarity between resume and job vectors
    Returns a float between 0.0 and 1.0
    """
    if not resume_vector or not job_vector:
        return 0.0

    resume_vec = np.array(resume_vector).reshape(1, -1)
    job_vec = np.array(job_vector).reshape(1, -1)

    score = cosine_similarity(resume_vec, job_vec)[0][0]
    return float(score)


def rank_jobs_for_user(user, top_n=10):
    """
    Rank jobs for a user based on cosine similarity
    """
    profile = user.profile

    if not profile.resume_vector:
        return []

    resume_vector = profile.resume_vector

    jobs = Job.objects.exclude(job_vector__isnull=True)

    scored_jobs = []

    for job in jobs:
        score = compute_similarity(resume_vector, job.job_vector)

        scored_jobs.append({
            "job": job,
            "score": round(score, 4)
        })

    # Sort highest similarity first
    scored_jobs.sort(key=lambda x: x["score"], reverse=True)

    return scored_jobs[:top_n]

def calculate_skill_gap(user_skills, job_skills):
    """
    Returns skills required by the job but missing from the user
    """
    user_set = normalize_skills(user_skills)
    job_set = normalize_skills(job_skills)

    missing = job_set - user_set
    return sorted(list(missing))