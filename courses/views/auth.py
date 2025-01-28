from django.shortcuts import render,redirect
from courses.models import Course, Video 
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from courses.forms import RegistrationForm
from courses.forms import LoginForm
from django.views import View
from django.contrib.auth import logout,login
from django.views.generic.edit import FormView 

class SignupView(FormView):
    template_name = 'courses/signup.html'
    form_class = RegistrationForm
    success_url = 'login'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'courses/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self,form):
        login(self.request,form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form) 


'''
#ye commented wala normal function based view hai 
class SignupView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,template_name = 'courses/signup.html',context={'form':form})

    def post(self,request):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            if (user is not None):
                return redirect('login')
        return render(request,template_name = 'courses/signup.html',context={'form':form})
'''
'''
class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            'form':form,
        }
        return render(request,'courses/login.html',context=context)
    
    def post(self,request):
        form = LoginForm(request=request,data=request.POST)
        context = {
            'form':form,
        }
        if(form.is_valid()):
                return redirect('home')
        return render(request,'courses/login.html',context=context)
'''

def signout(request):
    logout(request)
    return redirect('home')







