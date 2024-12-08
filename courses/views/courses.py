from django.shortcuts import HttpResponse
from django.shortcuts import render
from courses.models import Course


def coursePage(request,slug):

    courses = Course.objects.get(slug=slug) #pylint: disable=no-member
    print(slug,courses)
    return render(request,template_name='courses/course_page.html',context={'slug':slug,'course':courses})
    



  



