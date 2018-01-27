from django.shortcuts import render
from .models import Material, Deadline
from django.utils import timezone


def index(request):
    pinned_materials = Material.objects.filter(pinned=True)
    deadlines = Deadline.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'index.html', {
        'pinned_materials': pinned_materials,
        'deadlines': deadlines
    })


def materials(request):
    objs = Material.objects.filter(pinned=False)
    return render(request, 'materials.html', {'materials': objs})


def exams(request):
    return render(request, 'exams.html')
