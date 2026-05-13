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
- **SQLite** (default `db.sqlite3`)
- **Templates + static** CSS/JS (Bootstrap used on the add-job page)

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

## Demo checklist (good for submissions)

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

Add your **team names**, **course code**, and **semester** here before you submit.

---

## License

Specify your course policy (e.g. “All rights reserved” or an open license) before publishing publicly.
