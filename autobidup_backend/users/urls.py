from django.urls import path
# from .views import RegisterView,LoginView,CustomerView,ChangePasswordView,UpdateInfoView
from .views import LogoutView,RegisterView,LoginView,CustomerView,ChangePasswordView,UpdateInfoView,VerifyOTP


urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('customer-details',CustomerView.as_view()),
    path('change-password',ChangePasswordView.as_view()),
    path('update-customer',UpdateInfoView.as_view()),
    path('otp-verify',VerifyOTP.as_view()),
    path('logout',LogoutView.as_view()),
]
