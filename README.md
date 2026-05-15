# JobFinder (Django)

JobFinder is a small job-board web app built with **Django**. Visitors can browse jobs, filter listings, sign up, log in, apply to open roles, see jobs they applied to, and withdraw an application. Staff with a **superuser** account can use a simple dashboard, list jobs in the database, and add new jobs through a form.

This project was built for a **Web Technology** course (Phase 3: implement the site in Django).

---

## Features

| Area | What it does |
|------|----------------|
| **Public** | Home page, job listing with search filters (title, experience, status), job detail pages |
| **Auth** | Sign up, log in, log out (session-based); login redirects superusers to the admin dashboard |
| **Applications** | Apply to **open** jobs only; cannot apply to **closed** jobs (UI + server validation); withdraw an existing application from the job detail page |
| **Applied jobs** | Logged-in users see jobs they have applied to, with links back to details |
| **Admin (superuser)** | Dashboard with live counts (users, open/closed jobs), manage jobs table from the database, add job form (creates real `Job` rows) |
| **Django admin** | Standard `/admin/` site for models (optional use) |

---

## Tech stack

- **Python 3** + **Django 6** ([Django documentation](https://docs.djangoproject.com/en/stable/))
- **SQLite** locally (`db.sqlite3`); **PostgreSQL** when `DATABASE_URL` is set (e.g. on Render)
- **Gunicorn** + **WhiteNoise** for production-style serving
- **Templates + static** CSS/JS (Bootstrap used on the add-job page)

---

## Go live (production-ready layout)

The repo is wired for a typical **PaaS** deploy (e.g. [Render](https://render.com/), [Railway](https://railway.app/)): environment variables, static files via WhiteNoise, and `gunicorn` as the HTTP server.

### 1. Install dependencies locally (includes production packages)

```bash
pip install -r requirements.txt
```

### 2. Environment variables

Copy `.env.example` to `.env` for local experiments (optional). On the host, set at least:

| Variable | Example | Notes |
|----------|---------|--------|
| `DJANGO_DEBUG` | `False` | Required for public sites |
| `DJANGO_SECRET_KEY` | long random string | Never commit real values |
| `DJANGO_ALLOWED_HOSTS` | `your-app.onrender.com` | Comma-separated, no `https://` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | `https://your-app.onrender.com` | Comma-separated **with** `https://` |
| `DATABASE_URL` | *(optional)* Postgres URL | If unset, SQLite is used |

If `DJANGO_DEBUG=False` and `DJANGO_SECRET_KEY` is missing, Django will **refuse to start** (by design).

### 3. Static files

Production builds run:

```bash
python manage.py collectstatic --no-input
```

(Render does this in `buildCommand` in `render.yaml`.)

### 4. Deploy on Render (example)

1. Push this repo to **GitHub**.  
2. In Render: **New → Blueprint** (or **Web Service**) and point at the repo.  
3. If you use the included `render.yaml`, after the first deploy open the service → **Environment** and set:
   - `DJANGO_ALLOWED_HOSTS` = your service hostname (e.g. `jobfinder-xxxx.onrender.com`)
   - `DJANGO_CSRF_TRUSTED_ORIGINS` = `https://jobfinder-xxxx.onrender.com`  
4. **Redeploy**. Create a superuser from Render **Shell**: `python manage.py createsuperuser`.

**Free tier note:** SQLite on a free web instance is OK for demos; the filesystem can reset when the instance restarts. For data you cannot lose, add **Render Postgres** (or similar) and set `DATABASE_URL`.

### 5. Other hosts

- **Railway / Fly.io**: same env vars; start command is effectively `gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT` (see `Procfile`).

---

## Project layout

```
Jobfinder-_Django/
├── manage.py
├── requirements.txt
├── myproject/          # settings, root URLconf, WSGI
├── jobs/               # Job model + migrations (single source of truth for job postings)
├── application/      # Application model, auth-related views, admin dashboard template
├── page/               # Public pages, URL wiring, job list/detail templates
└── static/             # CSS, JS, assets
```

---

## Prerequisites

- **Python 3.12+** (recommended) with `pip`
- On Windows, the **`py`** launcher is helpful if `python` is not on your PATH

---

## Setup and run (local)

### 1. Clone and enter the project

```bash
cd "/path/to/Jobfinder-_Django"
```

### 2. Virtual environment (recommended)

**Windows (Git Bash)**

```bash
py -3 -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
./.venv/Scripts/python.exe manage.py migrate
./.venv/Scripts/python.exe manage.py createsuperuser   # optional, for admin features
./.venv/Scripts/python.exe manage.py runserver
```

**Windows (PowerShell)**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

### 3. Open the site

- App: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Django admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Stop the server with **Ctrl+C** in the terminal.

---

## Demo checklist 

1. Register a normal user → log in → **Find Jobs** → open a job → **Apply** → **Applied Jobs** shows it.  
2. Open the same job again → you should see **Withdraw application**, not **Apply now** → withdraw → **Apply now** returns.  
3. Try a **closed** job → apply is blocked with a clear message (UI + server).  
4. Log in as **superuser** → **Dashboard** → **Company Jobs** → **Add New Job** → confirm the new row appears on **Find Jobs**.

---

## Environment and Git

- Copy **`.env` / secrets** pattern for production; the repo uses dev defaults (`DEBUG=True`).  
- **`.gitignore`** excludes `.venv/`, `db.sqlite3`, `__pycache__/`, `.idea/`, etc. Do not commit your virtualenv or local database if the course forbids it.

---

## Course alignment (Phase 3)

Phase 3 asks you to complete the site using Django. In this repo, server-rendered pages, forms, authentication, models, migrations, and AJAX-style apply/withdraw endpoints are implemented in Django—not as a static-only prototype.

---

## Authors / course

## Authors / course

**Team Members:**
- Youssef Maher
- Youssef Bilal
- Hamza Shawky
- Ziad Ahmed
- Yassmin
- Rawan

---

## License
This project was developed for academic purposes. All rights reserved. 
Not to be reused or redistributed without permission.
