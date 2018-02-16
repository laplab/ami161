from django.shortcuts import render
from .models import Material, Deadline
from django.utils import timezone


def deadlines(request):
    pinned_materials = Material.objects.filter(pinned=True)
    deadlines = Deadline.objects.filter(date__gte=timezone.now()).order_by('date')
    old_deadlines = Deadline.objects.filter(date__lt=timezone.now()).order_by('date')
    return render(request, 'deadlines.html', {
        'pinned_materials': pinned_materials,
        'deadlines': deadlines,
        'old_deadlines': old_deadlines
    })


def materials(request):
    objs = Material.objects.filter(pinned=False)
    return render(request, 'materials.html', {'materials': objs})


def exams(request):
    return render(request, 'exams.html')
