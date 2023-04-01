from django.shortcuts import render
# from .serializer import TicketSerializer,MechanicSerializer,ServiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import bidding_car,key_generator
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
        # if
        airbagsx=request.data['airbagsx']
        if ['alloy_wheelsx'] in request.data:
            alloy_wheelsx=request.data['alloy_wheelsx']
            car.alloy_wheels =alloy_wheelsx

        if ['immoblizerx'] in request.data:
            immoblizerx=request.data['immoblizerx']
            car.immoblizer =immoblizerx

        if ['acx'] in request.data:
            acx=request.data['acx']
            car.ac =acx

        if ['cool_boxx'] in request.data:
            cool_boxx=request.data['cool_boxx']
            car.cool_box =cool_boxx

        if ['folding_seatsx'] in request.data:
            folding_seatsx=request.data['folding_seatsx']
            car.folding_seats =folding_seatsx

        if ['power_door_locksx'] in request.data:
            power_door_locksx=request.data['power_door_locksx']
            car.power_door_locks =power_door_locksx

        if ['antibrakingsystemx'] in request.data:
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
        car.airbags =airbagsx
        car.save()
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



