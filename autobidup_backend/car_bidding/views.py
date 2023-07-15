from django.shortcuts import render
from .serializer import CarSerializer,CalenderSerializer
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import bidding_car,key_generator,bidding_calender,bidding_room,room_generator,bidding_car_image
from users.models import Customer
from users.serializer import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
import jwt,datetime
from django.template import loader
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
import boto3
from botocore.exceptions import ClientError


import boto3
from rest_framework.parsers import MultiPartParser, FormParser

class RegisterMiniForm(APIView):

    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        user = Customer.objects.filter(username=payload['username']).first()
        serializer = UserSerializer(user)
        dphone_no = serializer.data['contact']
        f_name = serializer.data['first_name']
        l_name = serializer.data['last_name']
        username1 = serializer.data['username']
        dname = f_name + ' ' + l_name
        dchassis_no = request.data['chassis_no']
        dengine_no = request.data['engine_no']
        dyear = request.data['year']
        dmake = request.data['make']
        dmodel = request.data['model']
        dmileage = request.data['mileage'] + ' km'
        dmodified = request.data['modified']
        dcar_location = request.data['car_location']
        dcar_type = request.data['car_type']
        key = key_generator()
        key = 'B' + str(key)

        if dchassis_no == '':
            raise AuthenticationFailed('Chassis number cannot be empty')

        new_recd = bidding_car(
            automatic_generated_bid_id=key,
            username=username1,
            name=dname,
            phone_no=dphone_no,
            chassis_no=dchassis_no,
            engine_no=dengine_no,
            year=dyear,
            make=dmake,
            model=dmodel,
            mileage=dmileage,
            modified=dmodified,
            car_type=dcar_type,
            car_location=dcar_location
        )

        new_recd.save()  # Save the bidding_car object to generate an id


        return Response({'name': new_recd.name,
            'automatic_generated_bid_id': new_recd.automatic_generated_bid_id,
            'username': new_recd.username,
            'phone_no': new_recd.phone_no,
            'chassis_no': new_recd.chassis_no,
            'engine_no': new_recd.engine_no,
            'year': new_recd.year,
            'make': new_recd.make,
            'model': new_recd.model,
            'mileage': new_recd.mileage,
            'modified': new_recd.modified,
            'car_type': new_recd.car_type,
            'car_location': new_recd.car_location,})
    
class RecordDetailsAPI(APIView):
    def get(self, request):
        bid_id=request.data['id']
        record = bidding_car.objects.filter(automatic_generated_bid_id=bid_id).first()
        if not record:
            return Response({'message': 'Record not found.'}, status=404)
        
        record_data = {
            'name': record.name,
            'automatic_generated_bid_id': record.automatic_generated_bid_id,
            'phone_no': record.phone_no,
            'chassis_no': record.chassis_no,
            'engine_no': record.engine_no,
            'year': record.year,
            'make': record.make,
            'model': record.model,
            'mileage': record.mileage,
            'modified': record.modified,
            'car_type': record.car_type,
            'car_location': record.car_location,
        }
        
        images = bidding_car_image.objects.filter(bidding_car__automatic_generated_bid_id=bid_id)
        image_urls = [image.image.url for image in images]
        
        data = {
            'record_details': record_data,
            'image_urls': image_urls
        }
        
        return Response(data)
    
class RecordDetailsAPIusername(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        user = Customer.objects.filter(username=payload['username']).first()
        serializer = UserSerializer(user)
        uname = serializer.data['username']
        print(uname)
        record = bidding_car.objects.filter(username=uname).first()
        print(record)
        if not record:
            return Response({'message': 'Record not found.'}, status=404)
        record_data = {
            'name': record.name,
            'automatic_generated_bid_id': record.automatic_generated_bid_id,
            'phone_no': record.phone_no,
            'chassis_no': record.chassis_no,
            'engine_no': record.engine_no,
            'year': record.year,
            'make': record.make,
            'model': record.model,
            'mileage': record.mileage,
            'modified': record.modified,
            'car_type': record.car_type,
            'car_location': record.car_location,
        }

        
        return Response(record_data)

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
        starting_bid=request.data['staring_bid']+' rps'


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
        car.starting_bid =starting_bid
        car.ad_description =ad_descriptionx
        car.bid_date =bid_datx
        car.bid_time =bid_timex
        car.save()
        images = request.FILES.getlist('images')  # Retrieve multiple uploaded images
        for image in images:
            bidding_car_image_instance = bidding_car_image.objects.create(image=image)
            car.images.add(bidding_car_image_instance)
        car.save()
        
        car=bidding_car.objects.filter(automatic_generated_bid_id=bid_id).first()

        # create_bidding_calender(car)
        return Response({
            'asd':car.ad_title,
            'asd':car.automatic_generated_bid_id
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


# def date_diff(future_date_str):
#     today = datetime.today()
#     future_date = datetime.strptime(future_date_str, '%Y-%m-%d')
#     diff = future_date - today
#     return diff.days

# def time_diff(future_time_str):
#     today = datetime.now().time()
#     future_time = datetime.strptime(future_time_str, '%H:%M:%S').time()
#     diff = datetime.combine(datetime.today(), future_time) - datetime.combine(datetime.today(), today)
#     return diff



def datetime_diff(future_date_str, future_time_str):
    today = datetime.datetime.now()
    future_datetime_str = f"{future_date_str} {future_time_str}"
    future_datetime = datetime.datetime.strptime(future_datetime_str, '%Y-%m-%d %H:%M:%S')
    diff = future_datetime - today
    return str(diff)





def create_bidding_calender(car):
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
    new_car.starting_bid =car.starting_bid 
    new_car.bid_datetime_left=datetime_diff(car.bid_date,car.bid_time)
    new_car.airbags =car.airbags 
    new_car.alloy_wheels =car.alloy_wheels 
    new_car.immoblizer =car.immoblizer 
    new_car.ac =car.ac 
    new_car.cool_box =car.cool_box 
    new_car.folding_seats =car.folding_seats 
    new_car.power_door_locks =car.power_door_locks 
    new_car.antibrakingsystem =car.antibrakingsystem 
    # new_car.bid_time_down=time_diff()
    new_car.save()

class difference_of_time(APIView):
    def post(self,request):
        bid_id=request.data['bids']
        car=bidding_car.objects.filter(automatic_generated_bid_id=bid_id).first()
        time_left=datetime_diff(car.bid_date,car.bid_time)

        return Response({
            'remainingtime':time_left
        })


class show_all_bidding_cars(ListAPIView):
    queryset=bidding_car.objects.all()
    serializer_class=CarSerializer


class show_bidding_calender(ListAPIView):
    queryset=bidding_calender.objects.all()
    serializer_class=CalenderSerializer


class search_bidding_calender(ListAPIView):
    queryset=bidding_calender.objects.all()
    serializer_class=CalenderSerializer
    filter_backends=[SearchFilter]
    search_fields=['automatic_generated_bid_id','chassis_no','automatic_generated_bid_id','year','make','model','mileage','modified','car_type','engine_type','engine_capacity','transmission','assembly','ad_title','ad_description','bid_date','bid_time','airbags','alloy_wheels','immoblizer','ac','cool_box','folding_seats','power_door_locks','antibrakingsystem',]


class search_all_bidding_cars(ListAPIView):
    queryset=bidding_car.objects.all()
    serializer_class=CarSerializer
    filter_backends=[SearchFilter]
    search_fields=['automatic_generated_bid_id','name','phone_no','chassis_no','engine_no','automatic_generated_bid_id','year','make','model','mileage','modified','car_type','car_location','miniform_approved','engine_type','engine_capacity','transmission','assembly','ad_title','ad_description','bid_date','bid_time','airbags','alloy_wheels','immoblizer','ac','cool_box','folding_seats','power_door_locks','antibrakingsystem',]


class allot_bidding_room(APIView):
    def post(self,request):
        automatic_generated_bid_id=request.data['bids']
        car=bidding_car.objects.filter(automatic_generated_bid_id=automatic_generated_bid_id).first()

        if len(car.room_id) > 1:
            raise AuthenticationFailed('Room already alloted')
        else:
            pass
        new_room=bidding_room.objects.create()    
        new_room.room_id=room_generator()
        new_room.automatic_generated_bid_id=car.automatic_generated_bid_id
        new_room.year =car.year 
        new_room.make =car.make 
        new_room.model =car.model 
        new_room.mileage =car.mileage 
        new_room.modified =car.modified 
        new_room.car_type =car.car_type 
        new_room.engine_type =car.engine_type 
        new_room.engine_capacity =car.engine_capacity 
        new_room.transmission =car.transmission 
        new_room.assembly =car.assembly 
        new_room.ad_title =car.ad_title 
        new_room.starting_bid =car.starting_bid 
        new_room.start_date =car.bid_date 
        new_room.start_time =car.bid_time 
        new_room.bid_datetime_left=datetime_diff(car.bid_date,car.bid_time)
        new_room.increase_bid='50000'
        new_room.current_bid='0'
        # new_room.current_bid=new_room.increase_bid
        new_room.save()
        car.room_id_alloted=True
        car.room_id=new_room.room_id
        car.save()

        return Response({
            'room_id_alloted':car.room_id
        })
    

class enter_bidding_room(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        bid_id=request.data['bids']
        car=bidding_car.objects.filter(automatic_generated_bid_id=bid_id).first()
        user.entred_bidding_room_id=car.room_id
        user.current_bid='0'
        user.save()
        return Response({
            'room entered':user.entred_bidding_room_id
        })


class exit_bidding_room(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        user.entred_bidding_room_id=''
        user.save()
        return Response({
            'room entered':user.entred_bidding_room_id
        })
    

class increase_bid(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        room_ids=user.entred_bidding_room_id
        print(room_ids)
        room=bidding_room.objects.filter(room_id=room_ids).first()
        user.current_bid=int(user.current_bid)+int(room.increase_bid)
        user.save()
        if int(room.current_bid) < int(user.current_bid):
            room.current_bid=user.current_bid
            room.save()
        
        highest_bidder_obj=check_highest_bid(room.room_id)
        print(highest_bidder_obj.first_name)
        if int(user.current_bid) > int(highest_bidder_obj.current_bid):
            room.highest_bidder=user.first_name
            room.higest_bid=user.current_bid
            room.save()
        
        
        return Response({
            'username':user.first_name,
            'current bid':user.current_bid,
            'room highest bid':room.higest_bid,
        })

def check_highest_bid(room_id):
    room=bidding_room.objects.filter(room_id=room_id).first()
    all_users=Customer.objects.filter(entred_bidding_room_id=room_id).all()
    for user in all_users:
        if user.current_bid==room.higest_bid:
            room.highest_bidder=user.first_name
            room.save()
            return user


