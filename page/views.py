from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from application.models import Application
from jobs.models import Job


def _superuser_only(user):
    return user.is_authenticated and user.is_superuser


def index(request):
    return render(request, "page/index.html")


@login_required(login_url="/login/")
@user_passes_test(_superuser_only)
@require_http_methods(["GET", "POST"])
def add_job(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        company = (request.POST.get("company") or "").strip()
        salary_raw = request.POST.get("salary") or "0"
        experience_raw = request.POST.get("experience") or "0"
        status = (request.POST.get("status") or "open").strip().lower()
        job_type = (request.POST.get("job_type") or "Full-time").strip()
        description = (request.POST.get("description") or "").strip()
        responsibilities = (request.POST.get("responsibilities") or "").strip()
        requirements = (request.POST.get("requirements") or "").strip()

        if not name or not company:
            messages.error(request, "Job name and company are required.")
            return redirect("add_job")
        try:
            salary = int(salary_raw)
            experience = int(experience_raw)
        except ValueError:
            messages.error(request, "Salary and experience must be numbers.")
            return redirect("add_job")

        if status not in ("open", "closed"):
            status = "open"

        Job.objects.create(
            name=name[:100],
            company=company[:100],
            salary=salary,
            experience=experience,
            job_type=job_type[:50],
            status=status,
            description=description
            or "Details will be provided by the employer.",
            responsibilities=responsibilities or "—",
            requirements=requirements or "—",
            posted_date=timezone.now().date(),
        )
        messages.success(request, "Job added successfully.")
        return redirect("add_job")

    recent_jobs = Job.objects.order_by("-id")[:10]
    return render(
        request,
        "page/add_job.html",
        {"recent_jobs": recent_jobs},
    )


@login_required(login_url="/login/")
@user_passes_test(_superuser_only)
def admin_jobs(request):
    jobs = Job.objects.all().order_by("-id")
    return render(request, "page/admin_jobs.html", {"jobs": jobs})


def edit_job(request):
    return render(request, "page/edit_job.html")


def search_results(request):
    return render(request, "page/search_results.html")


def jobs(request):
    all_jobs = Job.objects.all()
    title_search = request.GET.get("title")
    exp_search = request.GET.get("experience")
    status_search = request.GET.get("status")
    if title_search:
        all_jobs = all_jobs.filter(name__icontains=title_search)
    if exp_search:
        all_jobs = all_jobs.filter(experience__lte=exp_search)
    if status_search and status_search != "all":
        all_jobs = all_jobs.filter(status__iexact=status_search)

    context = {
        "jobs": all_jobs,
        "title": title_search,
        "experience": exp_search,
        "status": status_search,
    }
    return render(request, "page/jobs.html", context)


@ensure_csrf_cookie
def job_details(request, id):
    job = get_object_or_404(Job, id=id)
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Application.objects.filter(
            user=request.user, job=job
        ).exists()
    return render(
        request,
        "page/job_details.html",
        {"job": job, "has_applied": has_applied},
    )
