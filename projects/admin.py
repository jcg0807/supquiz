# projects/admin.py

from django.contrib import admin
from .models import Project # Import the Project model from models.py

# Register your models here.
admin.site.register(Project)

