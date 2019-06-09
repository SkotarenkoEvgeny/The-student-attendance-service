from django.contrib import admin

from students.models.group import Group
from students.models.student import Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)