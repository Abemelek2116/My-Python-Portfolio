from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)
    resume_vector = models.JSONField(null=True, blank=True)

    skills = models.ManyToManyField('jobs.Skill', blank=True)

    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    education = models.TextField(null=True, blank=True)
    certifications = models.TextField(null=True, blank=True)
    projects = models.TextField(null=True, blank=True)

    location = models.CharField(max_length=255, null=True, blank=True)
    experience_level = models.CharField(max_length=50, null=True, blank=True)

    job_preferences = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class ParsedResume(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    skills = models.JSONField(null=True, blank=True)
    education = models.JSONField(null=True, blank=True)
    experience = models.JSONField(null=True, blank=True)

    parsed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Parsed resume for {self.user.username}"
