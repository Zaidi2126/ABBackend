import random
import string
from django.db import models

# Create your models here.
def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(4))
    if Order.objects.filter(oid=key).exists():
        key = key_generator()
    return key

class Products(models.Model):
    pid = models.CharField(max_length=5)
    pname = models.CharField(max_length=100)
    images = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    ptype = models.CharField(max_length=5, blank=True)

class Order(models.Model):
    oid = models.CharField(max_length=5)
    cname = models.CharField(max_length=200)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    zipcode = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    date = models.DateField()
    product_ids = models.CharField(max_length=100)