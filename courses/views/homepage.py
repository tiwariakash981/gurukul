from django.shortcuts import HttpResponse
from django.shortcuts import render
from courses.models import Course
from django.views.generic import ListView


class HomePageView(ListView):
    template_name='courses/home.html'
    queryset= Course.objects.all()

#yaha bydefault context = object_list hota hai
#context_object_name = 'courses' ye use karne ka agar context ka use karna hai to 
#class based view zada prefer karte hai kyuki vo thoda zada sahi hai 



'''
def home(request):
    courses = Course.objects.all() #pylint: disable=no-member
    return render(request,template_name='courses/home.html',context={'courses':courses})
'''