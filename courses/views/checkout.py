import datetime
from time import time
from django.shortcuts import render,redirect
from courses.models import Course,Video,Payment,UserCourse
from project.settings import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


import razorpay 
client = razorpay.Client(auth=(KEY_ID,KEY_SECRET))


def checkout(request,slug):
    course = Course.objects.get(slug=slug)
    user = None
    if request.user.is_authenticated is False:
        return redirect('login')

    user = request.user
    action=request.GET.get('action')
    order=None
    payment = None
    error = None
    if action=='create_payment':
        try:
            user_course = UserCourse.objects.get(user = user,course = course)# pylint: disable=no-member
            error = 'you are already enrolled in this course'
        except:
            pass 
        
        if error is None:
            amount = int((course.price - (course.price * course.discount * 0.01))*100)
            currency = 'INR'
            notes = {
                'email':user.email,
                'name': f'{user.first_name} {user.last_name}'
            }

            reciept = f'gurukul-{int(time())}'
            order = client.order.create(# pylint: disable=no-member
                {'receipt':reciept,
                'notes':notes,
                'amount':amount,
                'currency':currency})

            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()


    context = {
        'course':course,
        'order':order,
        'payment':payment,
        'user':user,
        'error':error

    }
    
    return render(request,'courses/check-out.html',context)
 
a=time()
print(a)
# print('ygdjkhfsdshfuisdf',time())


@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        try:
            client.utility.verify_payment_signature(data)# pylint: disable=no-member
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id = razorpay_order_id)# pylint: disable=no-member
            payment.payment_id = razorpay_payment_id 
            payment.status = True 

            userCourse = UserCourse(user = payment.user,course = payment.course)
            userCourse.save()

            payment.user_course = userCourse
            payment.save()


            return render(request, template_name='courses/my_courses.html',context={})
        except:
            return HttpResponse('Invalid Payment Details')




