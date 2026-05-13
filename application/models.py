from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey("jobs.Job", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.job.name}"
