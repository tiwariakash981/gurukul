from django.contrib import admin
from django.urls import path,include 
from courses.views import HomePageView,coursePage,SignupView,LoginView,signout,checkout,verifyPayment,MyCourseList,predict,about,index


from django.conf.urls.static import static
from project.settings import MEDIA_ROOT,MEDIA_URL
 
# username: akash (for superuser)
# Email address: tiwariakash981@gmail.com
# password: tiwari


urlpatterns = [
    path('',index,name='index'),
    path('courses',HomePageView.as_view(),name='courses'),
    path('logout',signout,name='logout'),
    path('my-courses',MyCourseList.as_view(),name='my-courses'),
    path('signup',SignupView.as_view(),name='signup'),
    path('login',LoginView.as_view(),name='login'),
    path('course/<str:slug>',coursePage,name='coursepage'),
    path('check-out/<str:slug>',checkout,name='check-out'),
    path('verify_payment',verifyPayment,name='verify_payment'),
    path('mlmodel',predict,name='mlmodel'),
    path('about',about,name='about'),
    # path('index',index,name='index'),
    

    
]

urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)






