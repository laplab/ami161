from django.contrib import admin

from .models import Subject, Material, Deadline

admin.site.register([Subject, Material, Deadline])
