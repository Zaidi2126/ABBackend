import ast
import json
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

from django_filters.rest_framework import DjangoFilterBackend


class show_all_products(ListAPIView):
    queryset=Products.objects.all()
    serializer_class=StoreSerializer

class search_products(generics.ListAPIView):
    queryset=Products.objects.all()
    serializer_class=StoreSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['pname', 'price', 'ptype']
    filterset_fields = {
        'price': ['gte', 'lte'],  
    }

class place_order(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        
        product_ids = request.data.get('product_ids', [])
        quantities = request.data.get('quantity', [])

        product_ids = [x for x in product_ids.strip("[]").split(",")]
        print(product_ids)
        quantities = [int(x) for x in quantities.strip("[]").split(",")]

        for i in range(len(product_ids)):
            product_id = product_ids[i]
            quantity = quantities[i]
            try:
                product = Products.objects.get(id=product_id)
                if product.quantity < quantity:
                    return Response({'error': f'Insufficient stock for product {product_id}'})
                else:
                    product.quantity -= quantity
                    product.save()
            except Products.DoesNotExist:
                return Response({'error': f'Product {product_id} does not exist'})
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
        Oquantity = request.data['quantity']
        # Ostatus = "Pending"
        key=key_generator()
        Okey='O'+str(key)
        
        new_recd=Order(oid=Okey,cname=Ocname,fname=Ofname,lname=Olname,address=Oaddress,city=Ocity,phone=Ophone,email=Oemail,zipcode=Ozipcode,price=Oprice,date=Odate, product_ids=Opid, quantity=Oquantity)
        new_recd.save()
        return Response({
            'message':'order placed successfully!'
        })
    


class CancelOrder(APIView):
    def put(self, request, order_id):
        try:
            order = Order.objects.get(oid=order_id)
        except Order.DoesNotExist:
            return Response({"message": "Order does not exist."})

        if order.status == 'cancelled':
            return Response({"message": "Order is already cancelled."})

        # Update order status
        order.status = 'cancelled'
        order.save()

        product_ids = request.data.get('product_ids', [])
        quantities = request.data.get('quantity', [])

        product_ids = [x for x in product_ids.strip("[]").split(",")]
        print(product_ids)
        quantities = [int(x) for x in quantities.strip("[]").split(",")]

        for i in range(len(product_ids)):
            product_id = product_ids[i]
            quantity = quantities[i]
            try:
                product = Products.objects.get(id=product_id)
                product.quantity += quantity
                product.save()
            except Products.DoesNotExist:
                return Response({'error': f'Product {product_id} does not exist'})

        return Response({"message": "Order has been cancelled."})