from rest_framework import serializers
from .models import bidd
from rest_framework import serializers



class TestSerializer(serializers.Serializer):
    username=serializers.CharField()


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=bike_ticket
        fields=['name','address','phone_no','delivery_date','email','description','specify_service','total_price','status','automatic_generated_invoice_number','special_order','specify_mechanic','notes']
    def create(self, validated_data):
        tp=service.objects.filter(service_name=validated_data['specify_service']).first()
        validated_data['total_price']=tp.service_price
        validated_data['automatic_generated_invoice_number']=key_generator()
        print(validated_data['automatic_generated_invoice_number'])
        instance= self.Meta.model(**validated_data)
        instance.save()
        return instance



class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model=mechanic
        fields=['f_name','l_name']





class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=service
        fields=['service_name','service_price','service_duration','service_availability']


