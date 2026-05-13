from django.db import migrations, models
import django.db.models.deletion


def clear_applications(apps, schema_editor):
    Application = apps.get_model("application", "Application")
    Application.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0002_application_job_delete_applictions_application_job"),
        ("jobs", "0002_job_delete_addjob"),
    ]

    operations = [
        migrations.RunPython(clear_applications, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="application",
            name="job",
        ),
        migrations.DeleteModel(
            name="Job",
        ),
        migrations.AddField(
            model_name="application",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="jobs.job",
            ),
        ),
    ]
