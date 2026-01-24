from django.shortcuts import render, get_object_or_404
from jobs.models import Job

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "users/job_detail.html", {"job": job})
