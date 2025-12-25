from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'resume_file',        # your resume
            'bio',
            'profile_picture',
            'phone_number',
            'education',
            'certifications',
            'projects',
            'location',
            'experience_level',
            'job_preferences',
            'skills',
        ]