from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from users.forms import SignupForm
from users.forms import ProfileForm 
from users.models import Profile

# --------------------------------------------------
# Home page (after login)
# --------------------------------------------------
@login_required
def home(request):
    return render(request, 'users/home.html')

# --------------------------------------------------
# Sign up view
# --------------------------------------------------
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()          # Save the new user
            login(request, user)        # Automatically log the user in
            return redirect('home')     # Redirect to home after signup
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

# --------------------------------------------------
# Profile view
# --------------------------------------------------
@login_required
def profile_view(request):
    # Ensure the user has a profile; create if missing
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'users/profile.html', {'form': form})
