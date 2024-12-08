from django.contrib import admin
from django.urls import path,include 
from courses.views import home,coursePage
from django.conf.urls.static import static
from project.settings import MEDIA_ROOT,MEDIA_URL

# username: akash (for superuser)
# Email address: tiwariakash981@gmail.com
# password: tiwari


urlpatterns = [
    path('',home,name='home'),
    path('course/<str:slug>',coursePage,name='coursepage')
   
]

urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)






