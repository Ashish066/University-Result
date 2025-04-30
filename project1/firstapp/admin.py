from django.contrib import admin
from firstapp.models import Student
class StudentAdmin(admin.ModelAdmin):
# Register your models here.
    list_display=['id','name','roll_no','marks']
admin.site.register(Student,StudentAdmin)