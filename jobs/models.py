from django.db import models

class Job(models.Model):

    name = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    salary = models.IntegerField()

    experience = models.IntegerField()

    job_type = models.CharField(max_length=50)

    status = models.CharField(max_length=20)

    description = models.TextField()

    responsibilities = models.TextField()

    requirements = models.TextField()
    
    posted_date = models.DateField()

    def __str__(self):

        return self.name