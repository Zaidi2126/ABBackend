from django.contrib import admin
from .models import Customer
# Register your models here.


class Customer_Admin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'username', 'contact','is_verified']
admin.site.register(Customer,Customer_Admin)








