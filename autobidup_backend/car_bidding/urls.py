from django.urls import path
# from .views import RegisterView,LoginView,CustomerView,ChangePasswordView,UpdateInfoView
from .views import RecordDetailsAPIusername,RecordDetailsAPI,increase_bid,exit_bidding_room,enter_bidding_room,allot_bidding_room,difference_of_time,AcceptMiniForm,RegisterMiniForm,RegisterMainForm,show_all_bidding_cars,show_bidding_rooms,search_all_bidding_cars,search_bidding_calender


urlpatterns = [
    path('mainform',RegisterMainForm.as_view()),
    path('miniform',RegisterMiniForm.as_view()),
    path('accept_miniform',AcceptMiniForm.as_view()),
    path('show_all_bidding_cars',show_all_bidding_cars.as_view()),
    path('show_bidding_rooms',show_bidding_rooms.as_view()),
    path('search_all_bidding_cars',search_all_bidding_cars.as_view()),
    path('search_bidding_calender',search_bidding_calender.as_view()),
    path('difference_of_time',difference_of_time.as_view()),
    path('allot_bidding_room',allot_bidding_room.as_view()),
    path('enter_bidding_room',enter_bidding_room.as_view()),
    path('exit_bidding_room',exit_bidding_room.as_view()),
    path('increase_bid',increase_bid.as_view()),
    path('record_details',RecordDetailsAPI.as_view()),
    path('record_details_username',RecordDetailsAPIusername.as_view()),

    # path('check_highest_bid',check_highest_bid.as_view()),
]
