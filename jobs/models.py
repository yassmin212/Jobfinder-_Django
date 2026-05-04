from django.db import models

# Create your models here.
class AddJob(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField()
    status = models.CharField(max_length= 20)
    salary = models.IntegerField()

    def __str__(self):
        return self.title