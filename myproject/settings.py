"""
Django settings for myproject project.

Local: run without env vars (defaults to DEBUG=True, SQLite).

Production: set DJANGO_DEBUG=False, DJANGO_SECRET_KEY, DJANGO_ALLOWED_HOSTS,
and DATABASE_URL (e.g. PostgreSQL on Render). See .env.example and README.
"""

import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core flags (override with environment variables) ---
DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() in ("1", "true", "yes")

_env_secret = os.environ.get("DJANGO_SECRET_KEY")
if _env_secret:
    SECRET_KEY = _env_secret
elif DEBUG:
    SECRET_KEY = (
        "django-insecure-&0e-1612*x=#0s4ziho4m&ciw3#-m043qm(aocv+fbr08&8*44"
    )
else:
    raise ValueError(
        "DJANGO_SECRET_KEY must be set when DJANGO_DEBUG is False (production)."
    )

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get(
        "DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost"
    ).split(",")
    if h.strip()
]

CSRF_TRUSTED_ORIGINS = [
    x.strip()
    for x in os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if x.strip()
]

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

LOGIN_URL = "/login/"

INSTALLED_APPS = [
    "jobs",
    "application",
    "page",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myproject.wsgi.application"

# --- Database: SQLite locally; DATABASE_URL on hosts like Render ---
_default_sqlite_url = "sqlite:///" + str(BASE_DIR / "db.sqlite3").replace("\\", "/")
DATABASES = {
    "default": dj_database_url.config(
        default=_default_sqlite_url,
        conn_max_age=600,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}
