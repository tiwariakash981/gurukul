from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from courses.models import Course,Video,UserCourse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def my_courses(request):
    user = request.user
    user_course = UserCourse.objects.filter(user=user)
    context = {
        'user_courses':user_course
    }
    return render(request,template_name='courses/my_courses.html',context=context)


def coursePage(request,slug):

    course = Course.objects.get(slug=slug) #pylint: disable=no-member
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by('serial_number')
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number=serial_number,course=course)# pylint: disable=no-member

    if (video.is_preview is False):
            
        if (request.user.is_authenticated is False): 
            return redirect('login')
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user=user,course=course)

            except:
                return redirect('check-out',slug=course.slug)
    context = {
        'course':course,
        'video':video,
        'videos':videos,

    }
       
    return render(request,template_name='courses/course_page.html',
    context={'slug':slug,'course':course,'video':video,'videos':videos})
    



  



