from django.shortcuts import render,redirect
from projects.models import User,Project
from .forms import ProjectForm


def index(request):
    users = User.objects.all()
    data = {"users":users}
    return render(request,'index.html',context=data)

def projects(request):
    projects = Project.objects.all()
    # tag = projects.tags.all()
    print(projects)
    data = {"projects":projects}
    return render(request,'projects.html',context=data)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tag.all()
    return render(request, 'project.html',{'project':projectObj,'tags':tags})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')



    data = {'form':form}
    return render(request,'create-project.html',data)

