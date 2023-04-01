from django.db import models
from django.core.exceptions import ValidationError
import random
import string


# Create your models here.
def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(4))
    if bidding_car.objects.filter(automatic_generated_bid_id=key).exists():
        key = key_generator()
    return key
def validate_miniform_approved(value):
    if not value:
        raise ValidationError('Please approve mini form first.')

class bidding_car(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    chassis_no = models.CharField(max_length=100)
    engine_no = models.CharField(max_length=100)
    automatic_generated_bid_id = models.CharField(max_length=5)
    year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mileage = models.CharField(max_length=100)
    modified = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    car_location = models.CharField(max_length=100)
    miniform_approved = models.BooleanField(default=False)
    
    engine_type = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    engine_capacity = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    transmission = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    assembly = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    ad_title = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    ad_description = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    bid_date = models.DateField(default='2020-02-22' ,blank=True, validators=[validate_miniform_approved])
    bid_time = models.TimeField(default='00:00:00', blank=True, validators=[validate_miniform_approved])
    airbags = models.BooleanField(default=False, validators=[validate_miniform_approved])
    alloy_wheels = models.BooleanField(default=False, validators=[validate_miniform_approved])
    immoblizer = models.BooleanField(default=False, validators=[validate_miniform_approved])
    ac = models.BooleanField(default=False, validators=[validate_miniform_approved])
    cool_box = models.BooleanField(default=False, validators=[validate_miniform_approved])
    folding_seats = models.BooleanField(default=False, validators=[validate_miniform_approved])
    power_door_locks = models.BooleanField(default=False, validators=[validate_miniform_approved])
    antibrakingsystem = models.BooleanField(default=False, validators=[validate_miniform_approved])







class bidding_calender(models.Model):
    chassis_no = models.CharField(max_length=100)
    automatic_generated_bid_id = models.CharField(max_length=5)
    year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mileage = models.CharField(max_length=100)
    modified = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    engine_capacity = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    transmission = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    assembly = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    ad_title = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    ad_description = models.CharField(max_length=100, default='', blank=True, validators=[validate_miniform_approved])
    bid_date = models.DateField(default='2020-02-22' ,blank=True, validators=[validate_miniform_approved])
    bid_time = models.TimeField(default='00:00:00', blank=True, validators=[validate_miniform_approved])
    airbags = models.BooleanField(default=False, validators=[validate_miniform_approved])
    alloy_wheels = models.BooleanField(default=False, validators=[validate_miniform_approved])
    immoblizer = models.BooleanField(default=False, validators=[validate_miniform_approved])
    ac = models.BooleanField(default=False, validators=[validate_miniform_approved])
    cool_box = models.BooleanField(default=False, validators=[validate_miniform_approved])
    folding_seats = models.BooleanField(default=False, validators=[validate_miniform_approved])
    power_door_locks = models.BooleanField(default=False, validators=[validate_miniform_approved])
    antibrakingsystem = models.BooleanField(default=False, validators=[validate_miniform_approved])