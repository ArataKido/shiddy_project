from django.shortcuts import render
from django.views.generic import ListView, DetailView

from case.models import Case


class Cases(ListView):
    template_name = 'theme/pages/case-studies.html'
    model = Case
    context_object_name = 'cases'


class CaseDetail(DetailView):
    """ Портфолио """
    template_name = 'theme/pages/detail/case-single.html'
    model = Case
    context_object_name = 'product'
