from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models.exams import Exams


def exam_list(request):

    exams = Exams.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('subjekt_name', 'date_time', 'teacher_name', 'title'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == 1:
            exams = exams.reverse()

    #paginate exam_list

    paginator = Paginator(exams, 1)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exams = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        exams = paginator.page(paginator.num_pages)


    return render(request, 'students/exam_list.html',
                  {'exams': exams})


def exam_add(request):
    return HttpResponse('<h1>Add exam</h1>')

def exam_edit(request, rit):
    return HttpResponse('<h1>Edit exam %s</h1>' % rit)

def exam_delete(request, rit):
    return HttpResponse('<h1>Delete exam %s</h1>' % rit)