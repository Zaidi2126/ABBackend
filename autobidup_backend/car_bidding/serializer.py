from rest_framework import serializers
from .models import bidding_car,bidding_calender
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=bidding_car
        fields=['automatic_generated_bid_id','name','phone_no','chassis_no','engine_no','automatic_generated_bid_id','year','make','model','mileage','modified','car_type','car_location','miniform_approved','engine_type','engine_capacity','transmission','assembly','ad_title','ad_description','bid_date','bid_time','airbags','alloy_wheels','immoblizer','ac','cool_box','folding_seats','power_door_locks','antibrakingsystem',]


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model=bidding_calender
        fields=['automatic_generated_bid_id','chassis_no','automatic_generated_bid_id','year','make','model','mileage','modified','car_type','engine_type','engine_capacity','transmission','assembly','ad_title','ad_description','bid_date','bid_time','airbags','alloy_wheels','immoblizer','ac','cool_box','folding_seats','power_door_locks','antibrakingsystem',]


























# name
# phone_no
# chassis_no
# engine_no
# automatic_generated_bid_id
# year
# make
# model
# mileage
# modified
# car_type
# car_location
# miniform_approved
# engine_type
# engine_capacity
# transmission
# assembly
# ad_title
# ad_description
# bid_date
# bid_time
# airbags
# alloy_wheels
# immoblizer
# ac
# cool_box
# folding_seats
# power_door_locks
# antibrakingsystem