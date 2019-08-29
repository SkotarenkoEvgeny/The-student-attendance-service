from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from django.views.generic import UpdateView, DeleteView, CreateView


from students.models.group import Group

# Views for Group

def groups_list(request):

    group_list = Group.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        group_list = group_list.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            group_list = group_list.reverse()

    # paginate students_list

    paginator = Paginator(group_list, 2)
    page = request.GET.get('page')
    try:
        group_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        group_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        group_list = paginator.page(paginator.num_pages)

    return render(request, 'students/groups.html', {'groups': group_list})

class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_create.html'
    fields = ('title', 'leader', 'notes')

    def get_success_url(self):
        return u'%s?status_message=Групу успішно збережено!' % reverse(
            'home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('reset'):
            return HttpResponseRedirect(
                u'%s?status_message=Додавання відмінено!', reverse('home'))
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)


def groups_add(requests):
    return HttpResponse('<h1>Groups add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Student %s</h1>' % gid)

# Views for Journal

def journal_main_view(requests):
    return render(requests, 'students/visits.html')
