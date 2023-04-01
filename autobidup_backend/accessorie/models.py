from django.db import models

# Create your models here.


class Products(models.Model):
    pid = models.CharField(max_length=5)
    pname = models.CharField(max_length=100)
    images = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()