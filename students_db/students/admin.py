from django.contrib import admin

from students.models.group import Group
from students.models.student import Student
from students.models.exams import Exams

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)


class ExamsAdmin(admin.ModelAdmin):
    list_display = ("subjekt_name", "date_time", "teacher_name", "title")


admin.site.register(Exams, ExamsAdmin)
