import random
import string
from django.db import models

# Create your models here.
def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(5))
    if UsedCars.objects.filter(cid=key).exists():
        key = key_generator()
    return key


class UsedCars(models.Model):
    cname = models.EmailField(null=True)
    cid = models.CharField(max_length=6)
    bodytype = models.CharField(max_length=100)
    reg_city = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    mileage = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    created_at = models.DateField()
    variant = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=200)
    engine_capacity = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    assembly = models.CharField(max_length=200)
    description = models.TextField()
    seller_name = models.CharField(max_length=200)
    seller_phone = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    images = models.ImageField(upload_to='car_images')
    airbags = models.BooleanField(default=False, null=True, blank=True)
    airconditioner = models.BooleanField(default=False, null=True, blank=True)
    alloywheels = models.BooleanField(default=False, null=True, blank=True)
    antilockbreakingsystem = models.BooleanField(default=False, null=True, blank=True)
    coolbox = models.BooleanField(default=False, null=True, blank=True)
    cupholders = models.BooleanField(default=False, null=True, blank=True)
    foldingrearseat = models.BooleanField(default=False, null=True, blank=True)
    immobilizer = models.BooleanField(default=False, null=True, blank=True)
    powerdoorlocks = models.BooleanField(default=False, null=True, blank=True)
    powersteering = models.BooleanField(default=False, null=True, blank=True)
    powerwindows = models.BooleanField(default=False, null=True, blank=True)
    powermirrors = models.BooleanField(default=False, null=True, blank=True)
    rearwiper = models.BooleanField(default=False, null=True, blank=True)
    tractioncontrol = models.BooleanField(default=False, null=True, blank=True)
    rearseatent = models.BooleanField(default=False, null=True, blank=True)
    climatecontrol = models.BooleanField(default=False, null=True, blank=True)
    rearacvents = models.BooleanField(default=False, null=True, blank=True)
    frontspeaker = models.BooleanField(default=False, null=True, blank=True)
    rearspeaker = models.BooleanField(default=False, null=True, blank=True)
    armrests = models.BooleanField(default=False, null=True, blank=True)
#     images = models.ManyToManyField('used_car_image', blank=True)



# class used_car_image(models.Model):
#     image = models.ImageField(upload_to='car_images/')