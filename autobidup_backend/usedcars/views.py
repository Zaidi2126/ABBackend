import jwt,datetime
from users.models import Customer
from rest_framework.views import APIView
from .models import UsedCars,key_generator
from .serializer import UsedCarsSerializer
from users.serializer import UserSerializer
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import AuthenticationFailed
from django_filters.rest_framework import DjangoFilterBackend


class show_all_cars(ListAPIView):
    queryset=UsedCars.objects.all()
    serializer_class = UsedCarsSerializer


class search_cars(generics.ListAPIView):
    queryset=UsedCars.objects.all()
    serializer_class=UsedCarsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['make','year', 'variant', 'price','bodytype']
    filterset_fields = {
        'price': ['gte', 'lte'],
        'year': ['gte', 'lte'],
    }


class create_post(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        print(request.data)
        user=Customer.objects.filter(username=payload['username']).first()
        serializer=UserSerializer(user)
        cname=serializer.data['username']
        # cid=request.data['cid']
        bodytype=request.data['bodytype']
        reg_city=request.data['reg_city']
        city=request.data['city']
        color=request.data['color']
        mileage=request.data['mileage']
        year=request.data['year']
        make=request.data['make']
        model=request.data['model']
        created_at=request.data['created_at']
        variant=request.data['variant']
        engine_type=request.data['engine_type']
        engine_capacity=request.data['engine_capacity']
        transmission=request.data['transmission']
        assembly=request.data['assembly']
        description=request.data['description']
        seller_name=request.data['seller_name']
        seller_phone=request.data['seller_phone']
        price=request.data['price']
        images=request.data['images']
        airbags=request.data['airbags']
        airconditioner=request.data['airconditioner']
        alloywheels=request.data['alloywheels']
        antilockbreakingsystem=request.data['antilockbreakingsystem']
        coolbox=request.data['coolbox']
        cupholders=request.data['cupholders']
        foldingrearseat=request.data['foldingrearseat']
        immobilizer=request.data['immobilizer']
        powerdoorlocks=request.data['powerdoorlocks']
        powersteering=request.data['powersteering']
        powerwindows=request.data['powerwindows']
        powermirrors=request.data['powermirrors']
        rearwiper=request.data['rearwiper']
        tractioncontrol=request.data['tractioncontrol']
        rearseatent=request.data['rearseatent']
        climatecontrol=request.data['climatecontrol']
        rearacvents=request.data['rearacvents']
        frontspeaker=request.data['frontspeaker']
        rearspeaker=request.data['rearspeaker']
        armrests=request.data['armrests']
        key=key_generator()
        Ckey='C'+str(key)
        new_recd=UsedCars(cname=cname,cid=Ckey,bodytype=bodytype,reg_city=reg_city,city=city,color=color,mileage=mileage,year=year,make=make,model=model,created_at=created_at, variant=variant, engine_type=engine_type,engine_capacity=engine_capacity,transmission=transmission,assembly=assembly,description=description,seller_name=seller_name,seller_phone=seller_phone,price=price,images=images,airbags=airbags,airconditioner=airconditioner, alloywheels=alloywheels, antilockbreakingsystem=antilockbreakingsystem,coolbox=coolbox,cupholders=cupholders,foldingrearseat=foldingrearseat,immobilizer=immobilizer,powerdoorlocks=powerdoorlocks,powersteering=powersteering,powerwindows=powerwindows,powermirrors=powermirrors,rearwiper=rearwiper,tractioncontrol=tractioncontrol, rearseatent=rearseatent, climatecontrol=climatecontrol,rearacvents=rearacvents,frontspeaker=frontspeaker,rearspeaker=rearspeaker,armrests=armrests)
        new_recd.save()
        # images = request.FILES.getlist('images')  # Retrieve multiple uploaded images
        # for image in images:
        #     used_car_image_instance = used_car_image.objects.create(image=image)
        #     new_recd.images.add(used_car_image_instance)
        return Response({
            'message':'post created successfully!'
        })


class remove_post(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        cid=request.data['cid']
        mt=UsedCars.objects.filter(cid=cid)
        print(mt)
        mt.delete()
        return Response({
           "post deleted"
        })


class edit_post(APIView):
    def post(self, request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        cid=request.data['cid']
        existing_post = UsedCars.objects.get(cid=cid)

        existing_post.bodytype = request.data.get('bodytype', existing_post.bodytype)
        existing_post.reg_city = request.data.get('reg_city', existing_post.reg_city)
        existing_post.city = request.data.get('city', existing_post.city)
        existing_post.color = request.data.get('color', existing_post.color)
        existing_post.mileage = request.data.get('mileage', existing_post.mileage)
        existing_post.year = request.data.get('year', existing_post.year)
        existing_post.make = request.data.get('make', existing_post.make)
        existing_post.model = request.data.get('model', existing_post.model)
        existing_post.variant = request.data.get('variant', existing_post.variant)
        existing_post.engine_type = request.data.get('engine_type', existing_post.engine_type)
        existing_post.engine_capacity = request.data.get('engine_capacity', existing_post.engine_capacity)
        existing_post.transmission = request.data.get('transmission', existing_post.transmission)
        existing_post.assembly = request.data.get('assembly', existing_post.assembly)
        existing_post.description = request.data.get('description', existing_post.description)
        existing_post.seller_name = request.data.get('seller_name', existing_post.seller_name)
        existing_post.seller_phone = request.data.get('seller_phone', existing_post.seller_phone)
        existing_post.price = request.data.get('price', existing_post.price)
        existing_post.images = request.data.get('images', existing_post.images)
        existing_post.airbags = request.data.get('airbags', existing_post.airbags)
        existing_post.airconditioner = request.data.get('airconditioner', existing_post.airconditioner)
        existing_post.alloywheels = request.data.get('alloywheels', existing_post.alloywheels)
        existing_post.antilockbreakingsystem = request.data.get('antilockbreakingsystem', existing_post.antilockbreakingsystem)
        existing_post.coolbox = request.data.get('coolbox', existing_post.coolbox)
        existing_post.cupholders = request.data.get('cupholders', existing_post.cupholders)
        existing_post.foldingrearseat = request.data.get('foldingrearseat', existing_post.foldingrearseat)
        existing_post.immobilizer = request.data.get('immobilizer', existing_post.immobilizer)
        existing_post.powerdoorlocks = request.data.get('powerdoorlocks', existing_post.powerdoorlocks)
        existing_post.powersteering = request.data.get('powersteering', existing_post.powersteering)
        existing_post.powerwindows = request.data.get('powerwindows', existing_post.powerwindows)
        existing_post.powermirrors = request.data.get('powermirrors', existing_post.powermirrors)
        existing_post.rearwiper = request.data.get('rearwiper', existing_post.rearwiper)
        existing_post.tractioncontrol = request.data.get('tractioncontrol', existing_post.tractioncontrol)
        existing_post.rearseatent = request.data.get('rearseatent', existing_post.rearseatent)
        existing_post.climatecontrol = request.data.get('climatecontrol', existing_post.climatecontrol)
        existing_post.rearacvents = request.data.get('rearacvents', existing_post.rearacvents)
        existing_post.frontspeaker = request.data.get('frontspeaker', existing_post.frontspeaker)
        existing_post.rearspeaker = request.data.get('powermirrors', existing_post.rearspeaker)
        existing_post.armrests = request.data.get('armrests', existing_post.armrests)

        existing_post.save()

        return Response({'message': 'Post updated successfully'})