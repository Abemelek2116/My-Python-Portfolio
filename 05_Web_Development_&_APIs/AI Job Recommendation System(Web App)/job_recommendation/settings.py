"""
Django settings for job_recommendation project.
"""

import os
from pathlib import Path

# --------------------------------------------------
# Base
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
DEBUG = True
# DEBUG = os.getenv("DEBUG") == "True"
# --------------------------------------------------
# Hosts (KEEP SIMPLE)
# --------------------------------------------------

# --------------------------------------------------
# Media files
# --------------------------------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".app.github.dev",   # allow ALL Codespace preview URLs
]

# --------------------------------------------------
# CSRF / Cookies (DEV FIX)
# --------------------------------------------------
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = False

CSRF_TRUSTED_ORIGINS = [
    "https://*.app.github.dev",
]

# --------------------------------------------------
# Applications
# --------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local apps
    "users",
    "jobs",
    "matching",

    # Third-party
    "rest_framework",
    "django_crontab",
]

AUTH_USER_MODEL = "users.CustomUser"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_URL = '/login/'

# --------------------------------------------------
# LOGIN / LOGOUT REDIRECTS
# --------------------------------------------------
# After login (or after signup and auto-login)
LOGIN_REDIRECT_URL = 'home'   # redirect to the home page (name of the URL pattern)

# After logout
LOGOUT_REDIRECT_URL = 'login'  # redirect to login page



# --------------------------------------------------
# Middleware
# IMPORTANT: CSRF DISABLED FOR DEV
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # DISABLED
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------
# URLs / Templates
# --------------------------------------------------
ROOT_URLCONF = "job_recommendation.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "job_recommendation.wsgi.application"

# --------------------------------------------------
# Database (Docker / Postgres)
# --------------------------------------------------
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
"""
# --------------------------------------------------
# Database (SQLite for local dev)   


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# --------------------------------------------------
# Password validation
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------
# Internationalization
# --------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# Static files
# --------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


CRONJOBS = [
    ('0 * * * *', 'jobs.cron.fetch_jobs'),
]
