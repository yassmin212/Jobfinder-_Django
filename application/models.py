from django.db import models

# Create your models here.
class Applictions(models.Model):
    user = models.CharField(max_length=50)
    job = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user} - {self.job}"