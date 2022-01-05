from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Project, Document
from django.template import loader
from .forms import DocumentForm

# Create your views here.

def new_document(request):
    form = DocumentForm()
    context = {'form' : form}
    return render(request, 'archive/new_document.html', context)

def index_documents(request):
    context = {}
    documents = Document.objects.all()
    context['documents'] = documents
    return render(request, 'archive/documents.html', context)

def show_document(request, pk: int):
    context = {}
    document = get_object_or_404(Document, pk=pk)
    context['document'] = document
    return render(request, 'archive/show_document.html', context)

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