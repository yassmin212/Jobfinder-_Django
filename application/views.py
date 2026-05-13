from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from jobs.models import Job
from .models import Application


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "application/signup.html",
                {"error": "Username already exists"},
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        login(request, user)
        return redirect("/")

    return render(request, "application/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")
            else:
                return redirect("/")

        else:
            return render(
                request,
                "application/login.html",
                {"error": "Invalid username or password"},
            )

    return render(request, "application/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect("login")

    users_count = User.objects.count()
    open_jobs_count = Job.objects.filter(status__iexact="open").count()
    closed_jobs_count = Job.objects.filter(status__iexact="closed").count()

    return render(
        request,
        "application/admin-dashboard.html",
        {
            "users_count": users_count,
            "open_jobs_count": open_jobs_count,
            "closed_jobs_count": closed_jobs_count,
        },
    )


@login_required(login_url="/login/")
@require_POST
def apply_for_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Job not found."})

    if (job.status or "").strip().lower() == "closed":
        return JsonResponse(
            {
                "status": "error",
                "message": "This job is closed. Applications are no longer accepted.",
            }
        )

    user = request.user

    if Application.objects.filter(user=user, job=job).exists():
        return JsonResponse(
            {"status": "error", "message": "You already applied for this job!"}
        )

    Application.objects.create(user=user, job=job)
    return JsonResponse(
        {"status": "success", "message": "Application submitted successfully!"}
    )


@login_required(login_url="/login/")
@require_POST
def withdraw_application(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Job not found."})

    deleted, _ = Application.objects.filter(user=request.user, job=job).delete()
    if deleted == 0:
        return JsonResponse(
            {
                "status": "error",
                "message": "You do not have an application to withdraw for this job.",
            }
        )
    return JsonResponse(
        {
            "status": "success",
            "message": "Your application was withdrawn.",
        }
    )


@login_required(login_url="/login/")
def applied_jobs(request):
    my_applications = Application.objects.filter(user=request.user)
    return render(
        request,
        "page/applied_jobs.html",
        {"applications": my_applications},
    )
