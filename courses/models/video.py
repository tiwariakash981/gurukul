from django.db import models 
from courses.models import Course
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=20,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=100,null=False)
    is_preview = models.BooleanField(default=False)
    
    def __str__(self): # pylint: disable=invalid-str-returned
        return self.title
    
    
    






