from django.shortcuts import render
# from .serializer import TicketSerializer,MechanicSerializer,ServiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import bidding_car,key_generator,bidding_calender
from users.models import Customer
from users.serializer import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
import jwt,datetime
from django.template import loader
from rest_framework.filters import SearchFilter

class RegisterMiniForm(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        serializer=UserSerializer(user)
        dphone_no=serializer.data['contact']
        f_name=serializer.data['first_name']
        l_name=serializer.data['last_name']
        dname=f_name+' '+l_name
        dchassis_no=request.data['chassis_no']
        dengine_no=request.data['engine_no']
        dyear=request.data['year']
        dmake=request.data['make']
        dmodel=request.data['model']
        dmileage=request.data['mileage']+' km'
        dmodified=request.data['modified']
        dcar_location=request.data['car_location']
        dcar_type=request.data['car_type']
        key=key_generator()
        key='B'+str(key)
        if dchassis_no == '':
            raise AuthenticationFailed('Chasis numner Cannot be empty')
        new_recd=bidding_car(automatic_generated_bid_id=key,name=dname,phone_no=dphone_no,chassis_no=dchassis_no,engine_no=dengine_no,year=dyear,make=dmake,model=dmodel,mileage=dmileage,modified=dmodified,car_type=dcar_type,car_location=dcar_location)
        new_recd.save()
        return Response({
            'asd':'asd'
        })
    

class RegisterMainForm(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        bid_id=request.data['bids']
        car=bidding_car.objects.filter(automatic_generated_bid_id=bid_id).first()

        if car.miniform_approved==True:
            pass
        else:
            raise AuthenticationFailed('Mini Form not complete')
        
        engine_typex=request.data['engine_typex']
        transmissionx=request.data['transmissionx']
        engine_capacityx=request.data['engine_capacityx']+' cc'
        assemblyx=request.data['assemblyx']
        ad_titlex=request.data['ad_titlex']
        ad_descriptionx=request.data['ad_descriptionx']
        bid_datx=request.data['bid_datx']
        bid_timex=request.data['bid_timex']


        if 'airbagsx' in request.data:
            airbagsx=request.data['airbagsx']
            car.airbags =airbagsx

        if 'alloy_wheelsx' in request.data:
            alloy_wheelsx=request.data['alloy_wheelsx']
            car.alloy_wheels =alloy_wheelsx

        if 'immoblizerx' in request.data:
            immoblizerx=request.data['immoblizerx']
            car.immoblizer =immoblizerx

        if 'acx' in request.data:
            acx=request.data['acx']
            car.ac =acx

        if 'cool_boxx' in request.data:
            cool_boxx=request.data['cool_boxx']
            car.cool_box =cool_boxx

        if 'folding_seatsx' in request.data:
            folding_seatsx=request.data['folding_seatsx']
            car.folding_seats =folding_seatsx

        if 'power_door_locksx' in request.data:
            power_door_locksx=request.data['power_door_locksx']
            car.power_door_locks =power_door_locksx

        if 'antibrakingsystemx' in request.data:
            antibrakingsystemx=request.data['antibrakingsystemx']
            car.antibrakingsystem=antibrakingsystemx
        car.engine_type =engine_typex
        car.engine_capacity =engine_capacityx
        car.transmission =transmissionx
        car.assembly =assemblyx
        car.ad_title =ad_titlex
        car.ad_description =ad_descriptionx
        car.bid_date =bid_datx
        car.bid_time =bid_timex
        car.save()
        creates(car)
        return Response({
            'asd':'asd'
        })
    


class AcceptMiniForm(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        bid_id=request.data['bids']
        car=bidding_car.objects.filter(automatic_generated_bid_id=bid_id).first()
        car.miniform_approved=True
        car.save()

        return Response({
            'asd':'asd'
        })




def creates(car):
    new_car=bidding_calender.objects.create()
    new_car.automatic_generated_bid_id=car.automatic_generated_bid_id
    new_car.chassis_no =car.chassis_no 
    new_car.year =car.year 
    new_car.make =car.make 
    new_car.model =car.model 
    new_car.mileage =car.mileage 
    new_car.modified =car.modified 
    new_car.car_type =car.car_type 
    new_car.engine_type =car.engine_type 
    new_car.engine_capacity =car.engine_capacity 
    new_car.transmission =car.transmission 
    new_car.assembly =car.assembly 
    new_car.ad_title =car.ad_title 
    new_car.ad_description =car.ad_description 
    new_car.bid_time =car.bid_time 
    new_car.bid_date =car.bid_date 
    new_car.airbags =car.airbags 
    new_car.alloy_wheels =car.alloy_wheels 
    new_car.immoblizer =car.immoblizer 
    new_car.ac =car.ac 
    new_car.cool_box =car.cool_box 
    new_car.folding_seats =car.folding_seats 
    new_car.power_door_locks =car.power_door_locks 
    new_car.antibrakingsystem =car.antibrakingsystem 
    new_car.save()

    new_car.save()
    