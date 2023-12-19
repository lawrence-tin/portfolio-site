from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def home(request):
    name = "John Doe"
    project_categories = ['Automation', 'Web App Development', 'Backend']
    context = {
        'name': name,
        'project_categories': project_categories,
    }
    return render(request, 'projects/home.html', context)