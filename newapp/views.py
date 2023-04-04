from django.shortcuts import render
from .models import Students
from django.views.generic.list import ListView


class StudentList(ListView):
    model = Students
    template_name = 'base.html'