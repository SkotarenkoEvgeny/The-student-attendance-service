from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from django.views.generic import UpdateView, DeleteView, CreateView

from django.forms.models import ModelForm

from students.models.group import Group

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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


# The part of create group

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # add buttons
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('reset', 'Reset'))
        self.helper.add_input(
            Submit('cancel', 'Cancel', css_class='btn-danger'))


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'students/groups_create.html'

    def get_success_url(self):
        return u'%s?status_message=Групу успішно збережено!' % reverse(
            'home')

    def post(self, request, *args, **kwargs):
        # the Add-group form logic
        if 'cancel' in request.POST:
            return HttpResponseRedirect(
                u'%s?status_message=Додавання відмінено!' % reverse('groups'))
        elif 'reset' in request.POST:
            return HttpResponseRedirect(reverse('groups_add'))
        else:
            return super(GroupCreateView, self).post(request, *args, **kwargs)


# The part of Edit group

class GroupEditForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse('groups_edit', kwargs={
            'gid': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        # add buttons
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('reset', 'Reset'))
        self.helper.add_input(
            Submit('cancel', 'Cancel', css_class='btn-danger'))


class GroupEditView(UpdateView):
    model = Group
    form_class = GroupEditForm
    template_name = 'students/groups_create.html'
    pk_url_kwarg = 'gid'

    def get_success_url(self):
        return u'%s?status_message=Групу успішно збережено!' % reverse(
            'home')

    def post(self, request, *args, **kwargs):
        # the Edit-group form logic
        if 'cancel' in request.POST:
            return HttpResponseRedirect(
                u'%s?status_message=Редагування відмінено!' % reverse('groups'))
        elif 'reset' in request.POST:
            return HttpResponseRedirect(reverse('groups_add'))
        else:
            return super(GroupEditView, self).post(request, *args, **kwargs)


# The part for delete group

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_delete.html'
    pk_url_kwarg = 'gid'

    def get_success_url(self):
        return u'%s?status_message=Групу успішно видалено!' % reverse('home')


# Views for Journal

def journal_main_view(requests):
    return render(requests, 'students/visits.html')
