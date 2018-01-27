from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'materials$', views.materials, name='materials'),
    re_path(r'exams$', views.exams, name='exams'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
