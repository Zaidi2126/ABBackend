from django.shortcuts import render
from .serializer import StoreSerializer
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Products,key_generator, Order
from users.models import Customer
from users.serializer import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
import jwt,datetime
from django.template import loader
from rest_framework.filters import SearchFilter
from rest_framework import generics, filters

class show_all_products(ListAPIView):
    queryset=Products.objects.all()
    serializer_class=StoreSerializer

class search_products(generics.ListAPIView):
    queryset=Products.objects.all()
    serializer_class=StoreSerializer
    filter_backends=[filters.SearchFilter]
    search_fields = ['pid','pname', 'images', 'price', 'description','ptype']

class place_order(APIView):
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
        Ocname=serializer.data['username']
        Ofname=request.data['fname']
        Olname=request.data['lname']
        Oaddress=request.data['address']
        Ocity=request.data['city']
        Ophone=request.data['phone']
        Oemail=request.data['email']
        Ozipcode=request.data['zipcode']
        Oprice=request.data['price']
        Odate=request.data['date']
        Opid=request.data['product_ids']
        key=key_generator()
        Okey='O'+str(key)
        new_recd=Order(oid=Okey,cname=Ocname,fname=Ofname,lname=Olname,address=Oaddress,city=Ocity,phone=Ophone,email=Oemail,zipcode=Ozipcode,price=Oprice,date=Odate, product_ids=Opid)
        new_recd.save()
        return Response({
            'message':'order placed successfully!'
        })