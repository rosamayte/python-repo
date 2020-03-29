from django.contrib import admin

# Register your models here.

from .models import Project
from .models import Student


admin.site.register(Project)

admin.site.register(Student)
# model has been registered to admin
