from django.contrib import admin
from django.utils.html import format_html

from .models import File, Subject, Material, Deadline


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'download_url')
    list_display_links = ('name',)

    def download_url(self, obj):
        return format_html('<a href="/media/{0}">Download {0}</a>', obj.name)
    download_url.short_description = 'Storage link'


admin.site.register([Subject, Material, Deadline])
