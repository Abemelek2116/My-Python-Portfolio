from django.core.management.base import BaseCommand
from jobs.models import Job
from jobs.services import generate_job_vector


class Command(BaseCommand):
    help = "Generate vectors for all jobs"

    def handle(self, *args, **kwargs):
        jobs = Job.objects.all()
        count = 0

        for job in jobs:
            if not job.job_vector:
                generate_job_vector(job)
                count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Generated vectors for {count} jobs"
        ))
