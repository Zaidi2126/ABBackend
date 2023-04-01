from django.urls import path
# from .views import RegisterView,LoginView,CustomerView,ChangePasswordView,UpdateInfoView
from .views import AcceptMiniForm,RegisterMiniForm,RegisterMainForm,show_all_bidding_cars,show_bidding_calender,search_all_bidding_cars,search_bidding_calender


urlpatterns = [
    path('mainform',RegisterMainForm.as_view()),
    path('miniform',RegisterMiniForm.as_view()),
    path('accept_miniform',AcceptMiniForm.as_view()),
    path('show_all_bidding_cars',show_all_bidding_cars.as_view()),
    path('show_bidding_calender',show_bidding_calender.as_view()),
    path('search_all_bidding_cars',search_all_bidding_cars.as_view()),
    path('search_bidding_calender',search_bidding_calender.as_view()),
]
