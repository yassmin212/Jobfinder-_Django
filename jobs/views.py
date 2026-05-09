from django.shortcuts import render, get_object_or_404
from .models import Job


def jobs_list(request):

    jobs = Job.objects.all()

    title = request.GET.get('title', '')
    experience = request.GET.get('experience', '')
    status = request.GET.get('status', 'all')

    if title:
        jobs = jobs.filter(name__icontains=title)

    if experience:
        jobs = jobs.filter(experience__lte=experience)

    if status != "all":
        jobs = jobs.filter(status__iexact=status)

    return render(request, 'page/jobs.html', {

        'jobs': jobs,
        'title': title,
        'experience': experience,
        'status': status,

    })


def job_details(request, id):

    job = get_object_or_404(Job, id=id)

    return render(
        request,
        'page/job_details.html',
        {'job': job}
    )