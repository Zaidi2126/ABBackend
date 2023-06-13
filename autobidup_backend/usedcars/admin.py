from django.contrib import admin
from .models import UsedCars
# Register your models here.


class used_cars_Admin(admin.ModelAdmin):
    list_display = ['cname','cid','bodytype','reg_city','city','color','mileage','year','make','model','created_at','variant','engine_type','engine_capacity','transmission','assembly','description', 'seller_name', 'seller_phone', 'price','images','airbags','airconditioner','alloywheels','antilockbreakingsystem','coolbox','cupholders','foldingrearseat','immobilizer','powerdoorlocks','powersteering','powerwindows','powermirrors','rearwiper','tractioncontrol','rearseatent','climatecontrol','rearacvents','frontspeaker','rearspeaker','armrests']

admin.site.register(UsedCars, used_cars_Admin)