from django.urls import path
# from .views import RegisterView,LoginView,CustomerView,ChangePasswordView,UpdateInfoView
from .views import request_call,buy_calls,show_expert,search_mechanic,Allot_mechanic,Remove_mechanic,get_location
urlpatterns = [
    path('search_mechanic',search_mechanic.as_view()),
    path('allot_mechanic',Allot_mechanic.as_view()),
    path('remove_mechanic',Remove_mechanic.as_view()),
    path('show_experts',show_expert.as_view()),
    path('buy_calls',buy_calls.as_view()),
    path('request_call',request_call.as_view()),
    path('location',get_location.as_view()),
]
