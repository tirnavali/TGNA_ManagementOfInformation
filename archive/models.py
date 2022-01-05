from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProjectDetail(models.Model): 
    daily_criteria = models.PositiveSmallIntegerField() 
    completed = models.BooleanField()
    to_do = models.TextField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class Project(models.Model):
    name = models.CharField(max_length = 200)
    top_project = models.ForeignKey('self', verbose_name= ("Top Project"), related_name=("project"), on_delete=models.SET_NULL,blank=True, null=True)
    project_detail = models.OneToOneField(ProjectDetail, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name



    

class Qualification(models.Model):    
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class DocumentType(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Language(models.Model): 
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name



VACATION_COHICES= (
    ('tam','TAM'),
    ('yarım', 'YARIM'),
)

class Vacation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    vacation = models.CharField(max_length = 10, choices = VACATION_COHICES, default= 'tam')
    vacation_start_date = models.DateField(auto_now=False, auto_now_add=False, null=True) 
    vacation_end_date = models.DateField(auto_now=False, auto_now_add=False, null=True) 

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user)
    


class Document(models.Model):
    project = models.ForeignKey(Project, verbose_name=("Projects"), on_delete=models.SET_NULL, null=True)
    box = models.IntegerField()
    folder = models.IntegerField()
    qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True)  
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True) 
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Document object"