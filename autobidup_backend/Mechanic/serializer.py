from rest_framework import serializers
from .models import Mechanic,Mechanic_ticket,Expert
from rest_framework import serializers


class mechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mechanic
        fields=['name','phone_no','mechanic_id','assigned_customer_id','available']

class expertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expert
        fields=['name', 'phone_no','e_id','assigned_customer_id','description','skills']


class mechanicTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mechanic
        fields=['name','phone','location','description','m_id']
