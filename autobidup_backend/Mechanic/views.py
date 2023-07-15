import jwt
from django.http import JsonResponse
import requests
from users.models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import AuthenticationFailed
from .models import Mechanic,Mechanic_ticket,key_generator,Expert
from .serializer import expertSerializer,mechanicSerializer

from rest_framework import generics, filters

# Create your views here.


class search_mechanic(generics.ListAPIView):
    queryset=Mechanic.objects.all()
    serializer_class=mechanicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class Allot_mechanic(APIView):
    def post(self,request):
        if len(Mechanic.objects.filter(available=True)) ==0 :
            raise AuthenticationFailed("No mecanic avalible")
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        if user.alloted_mechanic !='':
            raise AuthenticationFailed('mec already assigined')
        mec=Mechanic.objects.filter(available=True).first()
        user.alloted_mechanic=mec.name
        user.save()
        mec.available=False
        mname=request.data['name']
        maddress=request.data['location']
        mdecription=request.data['description']
        mphone=request.data['phone']
        mm_id=user.alloted_mechanic
        key=key_generator()
        key='M'+str(key)
        new_recd=Mechanic_ticket(automatic_generated_M_ticket_id=key,name=mname,phone=mphone,location=maddress,description=mdecription,m_id=mm_id)
        new_recd.save()
        mec.assigned_m_ticket_id=key
        mec.save()
        return Response({
            'Mechanic id': mm_id
        })


class Remove_mechanic(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        if user.alloted_mechanic =='':
            raise AuthenticationFailed('NO mec assigined')
        mec=Mechanic.objects.filter(name=user.alloted_mechanic).first()
        user.alloted_mechanic=''
        user.save()
        mec.available=True
        mt=Mechanic_ticket.objects.filter(automatic_generated_M_ticket_id=mec.assigned_m_ticket_id).first()
        print(mt)
        mt.closed=True
        mec.assigned_m_ticket_id=''
        mt.delete()
        mt.save()
        mec.save()
        return Response({
           "Mecanic deleted"
        })


class show_expert(ListAPIView):
    queryset=Expert.objects.all()
    serializer_class=expertSerializer
    filter_backends=[SearchFilter]


class buy_calls(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.get(username=payload['username'])
        try:
            cCredit=request.data['credit']
            cCredit=int(cCredit)
            user.call_credit=user.call_credit+cCredit
            user.save()
            return Response({
            "call credit ":user.call_credit
            })
        except Exception as e:
            print(e)
            return Response({
            "message":"error"
            })


class request_call(APIView):
    def post(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('NOT AUTHENTICATED')
        user=Customer.objects.filter(username=payload['username']).first()
        id_of_e=request.data['expert_id']
        expert=Expert.objects.filter(e_id=id_of_e).first()
        expert.assigned_customer_id=user.contact
        expert.save()

        user.call_credit=user.call_credit-1
        user.save()
        return Response({
            'Assigined to':expert.name  ,
            'Assigined to':expert.assigned_customer_id  ,
            'left calls':  user.call_credit ,
        })

class get_location(APIView):
    def post(self,request):
        API_KEY = 'AIzaSyBzpF6wYSz1YjJ-9gZuzEwc4YIIFuj7NMA'
        ADDRESS = request.data['address']
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={ADDRESS}&key={API_KEY}'
        # url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}'

        response = requests.post(url)
        data = response.json()
        print(data)

        if 'results' in data:
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            return JsonResponse({'latitude': lat, 'longitude': lng})
        else:
            return JsonResponse({'error': 'Unable to get current location'}, status=500)