from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.models.student import Student
from students.models.group import Group

# Views for Students

def students_list(request):
    students = Student.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students_list

    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html',
                  {'students': students})


def students_add(request):

    print(request.method)
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            errors = {}
            if not errors:
                student = Student(
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    midle_name = request.POST['midle_name'],
                    birthday = request.POST['birthday'],
                    ticket = request.POST['ticket'],
                    student_group = Group.objects.get(pk=request.POST['student_group']),
                    photo = request.FILES.get('photo', '')
                )
                student.save()
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'students/student_form.html',
                              {'groups': Group.objects.all().order_by('title'), 'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'students/student_form.html',
                      {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)