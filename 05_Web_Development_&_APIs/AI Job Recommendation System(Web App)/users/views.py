# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Forms and models
from users.forms import SignupForm, ProfileForm
from users.models import Profile, ParsedResume

# Resume parser imports
from .parsers.text_extractor import extract_text
from .parsers.skills_parser import extract_skills
from .parsers.education_parser import extract_education
from .parsers.experience_parser import extract_experience


# --------------------------------------------------
# Helper function: Parse resume and save to ParsedResume
# --------------------------------------------------
def parse_resume(file, user):
    """
    Extract skills, education, experience from uploaded resume
    and save/update ParsedResume linked to the user.
    """
    # Extract text from file
    text = extract_text(file.path)

    # Extract sections
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)

    # Save to database
    ParsedResume.objects.update_or_create(
        user=user,
        defaults={
            "skills": skills,
            "education": education,
            "experience": experience
        }
    )


# --------------------------------------------------
# Home page (after login)
# --------------------------------------------------
@login_required
def home(request):
    """
    Landing page after login. Can show basic dashboard.
    """
    return render(request, 'users/home.html')


# --------------------------------------------------
# Sign up view
# --------------------------------------------------
def signup_view(request):
    """
    User registration. Auto-login after successful signup.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()           # Save user
            login(request, user)         # Auto-login
            return redirect('home')      # Redirect to home
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


# --------------------------------------------------
# Profile view
# --------------------------------------------------
@login_required
def profile_view(request):
    """
    View and edit user profile. 
    Parses resume automatically when uploaded.
    """
    # Ensure the user has a profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # Save profile updates

            # Parse the resume if uploaded
            if profile.resume_file:
                parse_resume(profile.resume_file, request.user)

            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/profile.html', {'form': form})
