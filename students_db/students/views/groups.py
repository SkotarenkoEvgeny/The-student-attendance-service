from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models.group import Group

# Views for Group

def groups_list(request):
    groups = (
        {'id': 1,
         'number': u'МтМ-21',
         'star': u'Ячменев Олег'},
        {'id': 2,
         'number': u'МтМ-22',
         'star': u'Подоба Віталій'}
    )
    return render(request, 'students/groups.html', {'groups': groups})


def groups_add(requests):
    return HttpResponse('<h1>Groups add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Student %s</h1>' % gid)

# Views for Journal

def journal_main_view(requests):
    return render(requests, 'students/visits.html')
