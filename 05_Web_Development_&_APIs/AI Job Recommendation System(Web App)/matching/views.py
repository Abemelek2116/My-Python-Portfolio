from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from users.models import ParsedResume
from jobs.models import Job
from jobs.services import calculate_skill_gap


@login_required
def skill_gap_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    parsed = ParsedResume.objects.filter(user=request.user).first()
    user_skills = parsed.skills if parsed else []

    job_skills = [skill.name for skill in job.required_skills.all()]

    missing_skills = calculate_skill_gap(user_skills, job_skills)

    return render(request, "matching/skill_gap.html", {
        "job": job,
        "missing_skills": missing_skills
    })
