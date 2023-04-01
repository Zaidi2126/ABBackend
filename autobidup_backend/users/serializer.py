from rest_framework import serializers
from .models import Customer

class UserSerializer( serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['last_name','first_name','username','password','contact','state','city','entred_bidding_room_id','current_bid']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        password= validated_data.pop('password',None)
        instance= self.Meta.model(**validated_data)
        if password is not True:
            instance.set_password(password)
        instance.save()
        return instance

class VerifyAccountSerializer(serializers.Serializer):
    username=serializers.EmailField()
    otp=serializers.CharField()
