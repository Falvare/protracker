from django.shortcuts import redirect, render
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Create your views here.
def projects(requests):
    projects = Project.objects.all
    return render(requests, 'projects/projects.html', {'projects':projects})

def createProject(requests):
    if requests.method == 'POST':
        form = ProjectForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/projects')
    else:
        form = ProjectForm()

    return render(requests, 'projects/add_project.html', {'form':form})

def projectDetails(requests, pk):
    project = Project.objects.get(pk=pk)
    return render(requests, 'projects/project_details.html', {'project':project})