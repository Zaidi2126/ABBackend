from rest_framework import serializers
from .models import UsedCars
from rest_framework import serializers


class UsedCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsedCars
        fields = ['cname','cid','bodytype','reg_city','city','color','mileage','year','make','model','created_at','variant','engine_type','engine_capacity','transmission','assembly','description', 'seller_name', 'seller_phone', 'price','images','airbags','airconditioner','alloywheels','antilockbreakingsystem','coolbox','cupholders','foldingrearseat','immobilizer','powerdoorlocks','powersteering','powerwindows','powermirrors','rearwiper','tractioncontrol','rearseatent','climatecontrol','rearacvents','frontspeaker','rearspeaker','armrests']