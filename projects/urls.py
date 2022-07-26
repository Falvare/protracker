from django.urls import path 
from .views import projects, createProject, projectDetails

urlpatterns = [
    path('', projects, name='projects'),
    path('projects/', projects, name='projects'),
    path('create-project/', createProject, name='create project'),
    path('project-details/<int:pk>', projectDetails, name='project details'),
]
