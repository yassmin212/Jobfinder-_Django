from django.shortcuts import render

# Create your views here.
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

def job1_details(request):
    return render(request, 'page/job1_details.html')

def job2_details(request):
    return render(request, 'page/job2_details.html')

def job3_details(request):
    return render(request, 'page/job3_details.html')

def jobs(request):
    return render(request, 'page/jobs.html')

def login(request):
    return render(request, 'page/login.html')

def search_results(request):
    return render(request, 'page/search_results.html')

def signup(request):
    return render(request, 'page/signup.html')