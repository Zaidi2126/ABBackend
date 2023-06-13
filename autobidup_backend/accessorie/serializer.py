from rest_framework import serializers
from .models import Products, Order
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields = ['pid','pname', 'images', 'price', 'description','ptype','quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = ["oid","cname", "fname", "lname", "address","city","phone","email","zipcode","price","date","product_ids",'quantity','status']