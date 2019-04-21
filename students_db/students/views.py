from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Views for Students
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'static/assets/images/smiley-1635449_640.png'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'static/assets/images/smiley-1635449_640.png'}
    )
    return render(request, 'students/students_list.html',
                  {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


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