from django.shortcuts import HttpResponse
from django.shortcuts import render
from courses.models import Course


def home(request):
    courses = Course.objects.all() #pylint: disable=no-member
    return render(request,template_name='courses/home.html',context={'courses':courses})