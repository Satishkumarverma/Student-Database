from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin 

@admin.register(Student)
class StudentAdminModel(ImportExportModelAdmin):
    list_display = ('id', 'name', 'clas', 'dob', 'gender', 'email', 'phone', 'address', 'state', 'image')
