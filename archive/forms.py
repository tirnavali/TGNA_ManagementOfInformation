from django import forms
from .models import Qualification, DocumentType, Language, Employee

class DocumentForm(forms.Form):
    box = forms.IntegerField(label="Box")
    folder = forms.IntegerField(label="Folder")
    qualification = forms.ModelChoiceField(queryset=Qualification.objects.all())
    document_type = forms.ModelChoiceField(queryset=DocumentType.objects.all())
    language = forms.ModelChoiceField(queryset=Language.objects.all())
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())