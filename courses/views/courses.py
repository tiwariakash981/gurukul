from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from courses.models import Course,Video


def coursePage(request,slug):

    course = Course.objects.get(slug=slug) #pylint: disable=no-member
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by('serial_number')
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number=serial_number,course=course)# pylint: disable=no-member
    if ((request.user.is_authenticated is False) and (video.is_preview is False)):
        return redirect('login')
       
    return render(request,template_name='courses/course_page.html',
    context={'slug':slug,'course':course,'video':video,'videos':videos})
    



  



