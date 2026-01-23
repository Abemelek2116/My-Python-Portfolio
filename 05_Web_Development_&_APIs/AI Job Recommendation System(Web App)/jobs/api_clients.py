import requests
from jobs.models import Job

REMOTEOK_API_URL = "https://remoteok.io/api"


def fetch_remoteok_jobs():
    """
    Fetch jobs from RemoteOK API.
    Returns a list of job dictionaries.
    """
    try:
        response = requests.get(
            REMOTEOK_API_URL,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        # First element is metadata → skip it
        return data[1:] if isinstance(data, list) else []

    except requests.RequestException as e:
        print("RemoteOK API error:", e)
        return []


def normalize_remoteok_job(api_job):
    """
    Convert RemoteOK job fields into our Job model fields
    """
    return {
        "title": api_job.get("position") or api_job.get("title"),
        "company": api_job.get("company"),
        "location": api_job.get("location") or "Remote",
        "description": api_job.get("description"),
        "apply_link": api_job.get("url"),
        "job_type": "Remote",
        "experience_level": "Not specified",
        "salary": api_job.get("salary"),
    }


def fetch_and_save_jobs():
    """
    Fetch jobs from RemoteOK and save/update them in DB
    """
    jobs = fetch_remoteok_jobs()

    for api_job in jobs:
        normalized = normalize_remoteok_job(api_job)

        Job.objects.update_or_create(
            title=normalized["title"],
            company=normalized["company"],
            defaults={
                "location": normalized["location"],
                "description": normalized["description"],
                "salary": normalized["salary"],
                "job_type": normalized["job_type"],
                "experience_level": normalized["experience_level"],
                "apply_link": normalized["apply_link"],
            }
        )
