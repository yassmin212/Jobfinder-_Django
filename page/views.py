from django.shortcuts import render


def index(request):
    return render(request, 'page/index.html')


def add_job(request):
    return render(request, 'page/add_job.html')


def admin_dashboard(request):
    return render(request, 'page/admin_dashboard.html')


def admin_jobs(request):
    return render(request, 'page/admin_jobs.html')


def applied_jobs(request):
    return render(request, 'page/applied_jobs.html')


def edit_job(request):
    return render(request, 'page/edit_job.html')


def login(request):
    return render(request, 'page/login.html')


def search_results(request):
    return render(request, 'page/search_results.html')


def signup(request):
    return render(request, 'page/signup.html')