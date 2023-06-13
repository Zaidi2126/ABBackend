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
    airbags = models.BooleanField(default=False)
    airconditioner = models.BooleanField(default=False)
    alloywheels = models.BooleanField(default=False)
    antilockbreakingsystem = models.BooleanField(default=False)
    coolbox = models.BooleanField(default=False)
    cupholders = models.BooleanField(default=False)
    foldingrearseat = models.BooleanField(default=False)
    immobilizer = models.BooleanField(default=False)
    powerdoorlocks = models.BooleanField(default=False)
    powersteering = models.BooleanField(default=False)
    powerwindows = models.BooleanField(default=False)
    powermirrors = models.BooleanField(default=False)
    rearwiper = models.BooleanField(default=False)
    tractioncontrol = models.BooleanField(default=False)
    rearseatent = models.BooleanField(default=False)
    climatecontrol = models.BooleanField(default=False)
    rearacvents = models.BooleanField(default=False)
    frontspeaker = models.BooleanField(default=False)
    rearspeaker = models.BooleanField(default=False)
    armrests = models.BooleanField(default=False)