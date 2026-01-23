from jobs.api_clients import fetch_and_save_jobs


def fetch_jobs():
    """
    Cron task: fetch jobs from APIs and save to DB
    """
    fetch_and_save_jobs()
