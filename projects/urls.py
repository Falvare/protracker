from django.urls import path 
from .views import projects, createProject, projectDetails, addTask, taskDetails

urlpatterns = [
    path('', projects, name='projects'),
    path('projects/', projects, name='projects'),
    path('create-project/', createProject, name='create project'),
    path('projects/<int:pk>', projectDetails, name='project details'),
    path('projects/<int:pk>/add-task', addTask, name='add task'),
    path('task-details/<int:pk>', taskDetails, name='task details'),
]
