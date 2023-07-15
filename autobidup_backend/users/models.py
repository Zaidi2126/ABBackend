from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Customer(AbstractUser):
    class Meta:
        verbose_name_plural = "Customers"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=2000000000000000000000000)
    contact = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    current_bid = models.CharField(max_length=200,default='',blank=True)
    alloted_mechanic = models.CharField(max_length=200,default='',blank=True)
    entred_bidding_room_id = models.CharField(max_length=200,default='',blank=True)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6,null=True,blank=True)
    REQUIRED_FIELDS= []
    call_credit=models.IntegerField(default=0)