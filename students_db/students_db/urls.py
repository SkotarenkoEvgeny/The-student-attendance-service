"""students_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from students.views import students, groups, journals, exams, contact_admin
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [

    # Students urls
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students.StudentUpdateView.as_view(),
        name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$',
        students.StudentDeleteView.as_view(),
        name='students_delete'),
    url(r'^$', students.students_list, name='home'),

    # Groups urls
    url(r'^groups/add/$', groups.GroupCreateView.as_view(), name='groups_add'),
    url(r'^groups/(?P<gid>.+)/edit/$', groups.GroupEditView.as_view(),
        # groups.groups_edit,
        name='groups_edit'),
    url(r'^groups/(?P<gid>.+)/delete/$', groups.GroupDeleteView.as_view(),
        name='groups_delete'),
    url(r'^groups/$', groups.groups_list, name='groups'),

    # Visits urls
    url(r'^journal/$', journals.journal_main_view, name='journal'),

    # Admin url
    url(r'^admin/', admin.site.urls),
    url(r'^contact-admin/$', contact_admin.ContactForm.contact_admin,
        name='contact_admin'),

    # exams urls
    url(r'^exam/add/$', exams.ExamCreateView.as_view(), name='exam_add'),
    url(r'^exam/(?P<rit>.+)/edit/$', exams.ExamEditView.as_view(), name='exam_edit'),
    url(r'^exam/(?P<rit>.+)/delete/$', exams.exam_delete, name='exam_delete'),
    url(r'exam/', exams.exam_list, name='exam'),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # serve files from media folder
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
