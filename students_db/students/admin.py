from django.contrib import admin
from django.core.urlresolvers import reverse

from django.forms import ModelForm, ValidationError

from students.models.group import Group
from students.models.student import Student
from students.models.exams import Exams


class ExamsAdmin(admin.ModelAdmin):
    list_display = ("subjekt_name", "date_time", "teacher_name", "title")


class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        """
        Check if student is leader in any group.
        If yes, then ensure it's the same as selected group.
        """
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи',
                                  code='invalid')
        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket',
                     'notes']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'sid': obj.id})


class GroupFormAdmin(admin.ModelAdmin):
    """
    Check if a group is exist
    """
    pass


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title']
    ordering = ['title']
    list_editable = ['leader']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['title', 'leader']



# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exams, ExamsAdmin)
