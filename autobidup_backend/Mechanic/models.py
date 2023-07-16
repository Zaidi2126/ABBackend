from django.db import models
from django.core.exceptions import ValidationError
import random
import string


def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(4))
    if Mechanic_ticket.objects.filter(automatic_generated_M_ticket_id=key).exists():
        key = key_generator()
    return key


class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    mechanic_id = models.CharField(max_length=5)
    assigned_customer_id= models.CharField(max_length=100,blank=True)
    available = models.BooleanField(default=False)
    assigned_m_ticket_id= models.CharField(max_length=100,blank=True)


class Mechanic_ticket(models.Model):
    automatic_generated_M_ticket_id = models.CharField(max_length=5)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    location=models.CharField(max_length=500)
    description=models.CharField(max_length=10000)
    m_id=models.CharField(max_length=500)
    closed = models.BooleanField(default=False, blank=True)

class Expert(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    description = models.TextField()
    skills= models.CharField(max_length=100)
    available = models.BooleanField(default=False)
    e_id=models.CharField(max_length=500, blank=True)
    assigned_customer_id= models.CharField(max_length=100,blank=True)




