from django.urls import path 
from .views import projects, createProject

urlpatterns = [
    path('', projects, name='projects'),
    path('projects/', projects, name='projects'),
    path('create-project/', createProject, name='create project')
]
