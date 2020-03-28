from django.db import models

# Create your models here.

class Project(models.Model):
    medium_url = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.medium_url
