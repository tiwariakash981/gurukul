from django.contrib import admin
from courses.models import Course,Tag,Prerequisite,Learning,Payment,UserCourse
from courses.models import Video
from django.utils.html import format_html

class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,LearningAdmin,PrerequisiteAdmin,VideoAdmin]
    list_display = ['name','get_price','get_discount','active']
    list_filter = ('discount','active')

    def get_discount(self,course):
        return f'{course.discount} %' 
    get_discount.short_description = 'Description'
    

    def get_price(self,course):
        return f'₹{course.price}'
    get_price.short_description = 'Price'

class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['order_id','get_user','get_course','status']
    list_filter = ['status','course']

    def get_user(self, payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")
    get_user.short_description = 'User'

    def get_course(self, payment):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</a>")
    get_course.short_description = 'Course'


class UserCourseAdminModel(admin.ModelAdmin):
    model = UserCourse
    list_display = ['click','get_user','get_course']
    list_filter = ['course']

    def get_user(self, usercourse):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</a>")
    get_user.short_description = 'User'

    def get_course(self, usercourse):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{usercourse.course.id}'>{usercourse.course}</a>")
    get_course.short_description = 'Course' 

    def click(self, usercourse):
        return 'Click to open'


 
admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment,PaymentAdmin) 
admin.site.register(UserCourse,UserCourseAdminModel)
 



















