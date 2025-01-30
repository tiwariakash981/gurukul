from django.shortcuts import render,redirect

def about(request):
    return render(request,template_name='courses/about.html')

def index(request):
    return render(request,template_name='courses/index.html')
    