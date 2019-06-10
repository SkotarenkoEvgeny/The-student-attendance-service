from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models.group import Group

# Views for Group

def groups_list(request):

    group_list = Group.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        group_list = group_list.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            group_list = group_list.reverse()

    return render(request, 'students/groups.html', {'groups': group_list})


def groups_add(requests):
    return HttpResponse('<h1>Groups add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Student %s</h1>' % gid)

# Views for Journal

def journal_main_view(requests):
    return render(requests, 'students/visits.html')
