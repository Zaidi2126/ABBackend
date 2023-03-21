from django.core.mail import send_mail
import random
from django.conf import settings 
from .models import Customer


def send_otp_via_email(email):
    subject='Your aacount verification email'
    otp= random.randint(1000,9999)
    message=f'Your otp is {otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj=Customer.objects.get(username=email)
    user_obj.otp=otp
    user_obj.save()