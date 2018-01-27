from django.contrib import admin

from .models import File, Subject, Material, Deadline

admin.site.register([File, Subject, Material, Deadline])
