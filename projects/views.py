from django.shortcuts import render, HttpResponse
from .models import Project, Task

# Create your views here.
def projects(requests):
    projects = Project.objects.all
    return render(requests, 'projects/projects.html', {'projects':projects})