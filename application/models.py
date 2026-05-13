from django.db import models
from django.contrib.auth.models import User # Make sure this is imported



class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE) # This links to Job model

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
