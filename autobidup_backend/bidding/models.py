from django.db import models
import random 
import string
# Create your models here.
def key_generator():
    key = 'B'.join(random.choice(string.digits) for x in range(4))
    if bidding_car.objects.filter(automatic_generated_invoice_number=key).exists():
        key = key_generator()
    return key

class bidding_car(models.Model):
    name=models.CharField(max_length=100,null=False)
    phone_no=models.CharField(max_length=20)
    chassis_no=models.CharField(max_length=100)
    engine_no=models.CharField(max_length=100)
    automatic_generated_bid_id=models.CharField(max_length=4,default='')
    year=models.CharField(max_length=100)
    make=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    mileage=models.CharField(max_length=100)
    modified=models.CharField(max_length=100)
    car_type=models.CharField(max_length=100)
    car_location=models.CharField(max_length=100)
    images_normal=models.ImageField(blank=True)
    allowed=models.BooleanField()
    # ----End OF MINI FORM-----
    engine_type=models.CharField(max_length=100,blank=True)
    engine_cap=models.CharField(max_length=100,blank=True)
    transmission=models.CharField(max_length=100,blank=True)
    Assembly=models.CharField(max_length=100,blank=True)
    air_bags=models.BooleanField(blank=True)
    alloy_wheels=models.BooleanField(blank=True)
    immoblizer=models.BooleanField(blank=True)
    ac=models.BooleanField(blank=True)
    coolbox=models.BooleanField(blank=True)
    power_door_locks=models.BooleanField(blank=True)
    abs=models.BooleanField(blank=True)
    folding_seats=models.BooleanField(blank=True)
    all_wheel_drive=models.BooleanField(blank=True)
    images_modeling=models.ImageField(blank=True)
    # ------Bidding details------
    bidding_title=models.CharField(max_length=100,blank=True)
    bidding_price=models.CharField(max_length=100,blank=True)
    bidding_desc=models.CharField(max_length=100,blank=True)
    bidding_date=models.DateField(blank=True)
    bidding_time=models.TimeField(blank=True)

   
    REQUIRED_FIELDS=[automatic_generated_bid_id]

    