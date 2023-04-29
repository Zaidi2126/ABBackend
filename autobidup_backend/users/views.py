from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer,VerifyAccountSerializer
from rest_framework.response import Response
from .models import Customer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from .emails import send_otp_via_email

# Create your views here.



class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_otp_via_email(serializer.data['username'])
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']     
        user=Customer.objects.filter(username=username).first()
        # passs=user.password
       

        if user is None:
            raise AuthenticationFailed('Wrong email')
        if not user.check_password(password):
            raise AuthenticationFailed('Wrong password')
        if user.is_verified==False:
            raise AuthenticationFailed('Please verify your account')
        
        payload={
            'username':user.username,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=2222),
            'iat':datetime.datetime.utcnow()

        }

        token=jwt.encode(payload,'secret',algorithm='HS256')
        response=Response() 
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token,
            'firstName':user.first_name,
            'lastName':user.last_name,
            'username':user.username,
            'username':user,
        }

        return response



class CustomerView(APIView):
    def get(self,request):
        
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        user=Customer.objects.filter(username=payload['username']).first()
        serializer=UserSerializer(user)
        


        return Response(serializer.data)
        





class ChangePasswordView(APIView):
    def post(self,request):
       #JWT AUTHERNTICATION
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')

        username=request.data['username']     
        password=request.data['password']     
        new_password=request.data['new_password']     
        re_enter_new_password=request.data['re_enter_new_password']     
        user=Customer.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('Wrong email')
        if not user.check_password(password):
            raise AuthenticationFailed('Wrong password')
        
        if new_password == re_enter_new_password:
            user=Customer.objects.filter(username=username).first()
            user.set_password(new_password)
            user.save()

        else:
            raise AuthenticationFailed('Passwords do not match!')

        # user=Customer.objects.filter(username=username).first()
        return Response({
            'Password Changed'
        })



class UpdateInfoView(APIView):
    def post(self,request):
       #JWT AUTHERNTICATION
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        serializer=UserSerializer(user)
        username=user.username
         
        if 'last_name' in request.data: 
            nlast_name=request.data['last_name']     
            user=Customer.objects.filter(username=username).update(last_name=nlast_name)
        if 'first_name' in request.data: 
            nfirst_name=request.data['first_name']     
            user=Customer.objects.filter(username=username).update(first_name=nfirst_name)
        if 'contact' in request.data: 
            ncontact=request.data['contact']     
            user=Customer.objects.filter(username=username).update(contact=ncontact)
        if 'state' in request.data: 
            nstate=request.data['state'] 
            user=Customer.objects.filter(username=username).update(state=nstate)
        if 'city' in request.data: 
            ncity=request.data['city']   
            user=Customer.objects.filter(username=username).update(city=ncity)
        if 'zip' in request.data: 
            nzip=request.data['zip']     
            user=Customer.objects.filter(username=username).update(zip=nzip)
        if 'street' in request.data: 
            nstreet=request.data['street']       
            user=Customer.objects.filter(username=username).update(street=nstreet)

        user=Customer.objects.filter(username=payload['username']).first()
        serializer=UserSerializer(user)
        
        
        return Response(serializer.data)



class VerifyOTP(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer= VerifyAccountSerializer(data=data)
            if serializer.is_valid():
                username=serializer.data['username']
                otp=serializer.data['otp']

                user=Customer.objects.filter(username=username)
                if not user.exists():
                    return Response({
                    'status':200,
                    'message': 'Registration sucessfull please check email ',
                    'data': serializer.data
                })

                user=user.first()
                if not user.otp == otp:
                    return Response({
                    'status':200,
                    'message': 'Wrong OTP ',
                    'data': serializer.data
                })
                user.is_verified= True
                user.save()
                return Response({
                    'status':200,
                    'message': 'Verified! ',
                    'data': serializer.data,
                })
            else:
                 return Response({
                    'message': 'Spmething went wrong'
                })
        except Exception as e:
            print(e)
            