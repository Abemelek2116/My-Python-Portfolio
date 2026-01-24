from django.urls import path
from . import views

urlpatterns = [
    path("skill-gap/<int:job_id>/", views.skill_gap_view, name="skill_gap"),
]
