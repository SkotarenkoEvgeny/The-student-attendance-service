from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, DeleteView
from django.forms.models import ModelForm
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from students.models.exams import Exams


def exam_list(request):
    exams = Exams.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('subjekt_name', 'date_time', 'teacher_name', 'title'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
    # paginate exam_list

    paginator = Paginator(exams, 2)
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


class ExamForm(ModelForm):
    class Meta:
        model = Exams
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        # add buttons
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('reset', 'Reset'))
        self.helper.add_input(
            Submit('cancel', 'Cancel', css_class='btn-danger'))


class ExamCreateView(CreateView):
    model = Exams
    form_class = ExamForm
    template_name = 'students/exam_create.html'

    def get_success_url(self):
        return u'%s?status_message=Іспит успішно збережено!' % reverse(
            'home')

    def post(self, request, *args, **kwargs):
        # the Add-group form logic
        if 'cancel' in request.POST:
            return HttpResponseRedirect(
                u'%s?status_message=Додавання відмінено!' % reverse('exam'))
        elif 'reset' in request.POST:
            return HttpResponseRedirect(reverse('exam_add'))
        else:
            return super(ExamCreateView, self).post(request, *args, **kwargs)

class ExamEditForm(ExamForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_action = reverse('exam_edit', kwargs={
            'rit': kwargs['instance'].id})


class ExamEditView(ExamCreateView, UpdateView):
    form_class = ExamEditForm
    pk_url_kwarg = 'rit'


def exam_delete(request, rit):
    return HttpResponse('<h1>Delete exam %s</h1>' % rit)
