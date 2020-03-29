
from __future__ import unicode_literals
from django.db import models


from djongo import models #Note the import method for mongo models



# Create your models here.

class Project(models.Model):
    medium_url = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.medium_url




class Student(models.Model): #Collection name
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    # Documents
    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField(default = 10, null=True)
    roll_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
