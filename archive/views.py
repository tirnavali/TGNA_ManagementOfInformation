from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Project
from django.template import loader

# Create your views here.

def index(request):
    projects = Project.objects.all()
    output = ",\n ".join([p.name for p in projects])
    template = loader.get_template('archive/index.html')
    context = {
        'projects' : projects
    }    
    return render(request, 'archive/index.html', context)

def show(request, project_id):
    #response = "Baktığınız kayıt %s."
    #return HttpResponse(response % project_id)
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'archive/show.html', {'project': project})