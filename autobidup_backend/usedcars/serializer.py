from rest_framework import serializers
from .models import UsedCars,used_car_image

class UsedCarImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = used_car_image
        fields = ['image_url']

    def get_image_url(self, obj):
        return obj.image.url

class UsedCarsSerializer(serializers.ModelSerializer):
    images = UsedCarImageSerializer(many=True, read_only=True)
    class Meta:
        model=UsedCars
        fields = ['cname','cid','bodytype','reg_city','city','color','mileage','year','make','model','created_at','variant','engine_type','engine_capacity','transmission','assembly','description', 'seller_name', 'seller_phone', 'price','images','airbags','airconditioner','alloywheels','antilockbreakingsystem','coolbox','cupholders','foldingrearseat','immobilizer','powerdoorlocks','powersteering','powerwindows','powermirrors','rearwiper','tractioncontrol','rearseatent','climatecontrol','rearacvents','frontspeaker','rearspeaker','armrests']