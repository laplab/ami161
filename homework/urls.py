from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'materials$', views.materials, name='materials'),
    re_path(r'exams$', views.exams, name='exams'),
]
