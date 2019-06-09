from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Views for Journal

def journal_main_view(requests):
    return render(requests, 'students/visits.html')