from django.contrib import admin
from .models import Project, Document, Qualification, DocumentType, Language
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Employee, Vacation
# Register your models here.

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class VacationInline(admin.StackedInline):
    model = Vacation
    can_delete = False
    verbose_name_plural = 'vacations'

class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, VacationInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Project)
admin.site.register(Document)
admin.site.register(Qualification)
admin.site.register(DocumentType)
admin.site.register(Language)
admin.site.register(Vacation)
