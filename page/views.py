from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import ensure_csrf_cookie

from jobs.models import Job


def index(request):
    return render(request, "page/index.html")


def add_job(request):
    return render(request, "page/add_job.html")


def admin_jobs(request):
    return render(request, "page/admin_jobs.html")


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
    return render(request, "page/job_details.html", {"job": job})
