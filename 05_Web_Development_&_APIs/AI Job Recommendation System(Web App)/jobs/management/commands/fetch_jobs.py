from django.core.management.base import BaseCommand
from jobs.api_clients import fetch_and_save_jobs


class Command(BaseCommand):
    help = "Fetch jobs from external APIs and save them to the database"

    def handle(self, *args, **kwargs):
        fetch_and_save_jobs()
        self.stdout.write(self.style.SUCCESS("Jobs fetched successfully"))
