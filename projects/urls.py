from django.urls import path
from .views import index,projects,project,createProject

urlpatterns = [
    path('',index,name='index'),
    path('projects/',projects,name='projects'),
    path('project/<str:pk>',project,name="project"),
    path('create-project/',createProject,name='createProject')

]
