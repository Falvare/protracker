from django.shortcuts import redirect, render, reverse
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
    tasks = Task.objects.filter(project=project)

    context = {
        'project':project,
        'tasks':tasks
        }
    return render(requests, 'projects/project_details.html', context=context)

def addTask(requests, pk):
    if requests.method == 'POST':
        form = TaskForm(requests.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = Project.objects.get(pk=pk)
            task.save()
            return redirect('/projects/' + str(pk))
    else:
        form = TaskForm()

    return render(requests, 'projects/add_task.html', {'form':form})