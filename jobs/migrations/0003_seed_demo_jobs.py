from datetime import date

from django.db import migrations


def seed_jobs(apps, schema_editor):
    Job = apps.get_model("jobs", "Job")
    if Job.objects.exists():
        return
    Job.objects.create(
        name="Backend Developer",
        company="TechCorp",
        salary=25000,
        experience=2,
        job_type="Full-time",
        status="open",
        description="Build and maintain APIs and services.",
        responsibilities="Design REST APIs\nCollaborate with frontend team\nWrite tests",
        requirements="Python\nDjango or similar\nSQL",
        posted_date=date(2026, 2, 1),
    )
    Job.objects.create(
        name="Frontend Developer",
        company="WebStudio",
        salary=20000,
        experience=1,
        job_type="Full-time",
        status="open",
        description="Implement responsive UIs with modern JavaScript.",
        responsibilities="Implement designs\nOptimize performance\nCode reviews",
        requirements="HTML/CSS\nJavaScript\nReact basics",
        posted_date=date(2026, 2, 10),
    )
    Job.objects.create(
        name="Data Analyst",
        company="Insight Ltd",
        salary=18000,
        experience=0,
        job_type="Contract",
        status="closed",
        description="Analyze business metrics and prepare reports.",
        responsibilities="Query databases\nBuild dashboards\nPresent findings",
        requirements="Excel\nSQL\nCommunication skills",
        posted_date=date(2026, 1, 15),
    )


def unseed_jobs(apps, schema_editor):
    Job = apps.get_model("jobs", "Job")
    Job.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0002_job_delete_addjob"),
    ]

    operations = [
        migrations.RunPython(seed_jobs, unseed_jobs),
    ]
