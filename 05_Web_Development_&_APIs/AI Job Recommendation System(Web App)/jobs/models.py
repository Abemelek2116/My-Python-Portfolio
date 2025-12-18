from django.db import models

# Create your models here.
from users.models import CustomUser, Profile

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    description = models.TextField()
    required_skills = models.ManyToManyField(Skill, blank=True)

    salary = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100)  # Full-time, remote, etc.
    experience_level = models.CharField(max_length=50)

    apply_link = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"


class Application(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    cover_letter = models.TextField(null=True, blank=True)
    resume_used = models.FileField(upload_to='application_resumes/', null=True, blank=True)

    ai_match_score = models.FloatField(null=True, blank=True)
    ai_feedback = models.TextField(null=True, blank=True)

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.job.title}"
