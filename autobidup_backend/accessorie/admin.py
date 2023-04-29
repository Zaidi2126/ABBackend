from django.contrib import admin
from .models import Products, Order
# Register your models here.


class accessories_car_Admin(admin.ModelAdmin):
    list_display = ["pid","pname", "images", "price", "description","ptype"]

class order_car_Admin(admin.ModelAdmin):
    list_display = ["oid","cname", "fname", "lname", "address","city","phone","email","zipcode","price","date","product_ids"]

admin.site.register(Products, accessories_car_Admin)
admin.site.register(Order, order_car_Admin)