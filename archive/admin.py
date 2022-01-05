from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Employee, Vacation
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('name','sub_projects_view')

    @admin.display(empty_value='none')
    def sub_projects_view(self, obj):
         return obj.project.all()

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
admin.site.register(SpecialNumberDetail)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDetail)
admin.site.register(Document)
admin.site.register(Qualification)
admin.site.register(DocumentType)
admin.site.register(Language)
admin.site.register(Vacation)
admin.site.register(Privacy)
admin.site.register(Toponym)
admin.site.register(Subject)
admin.site.register(Person)
admin.site.register(PhisycalStatus)
