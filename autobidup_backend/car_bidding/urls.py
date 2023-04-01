from django.urls import path
# from .views import RegisterView,LoginView,CustomerView,ChangePasswordView,UpdateInfoView
from .views import AcceptMiniForm,RegisterMiniForm,RegisterMainForm


urlpatterns = [
    path('mainform',RegisterMainForm.as_view()),
    path('miniform',RegisterMiniForm.as_view()),
    path('accept_miniform',AcceptMiniForm.as_view()),
    # path('create',create.as_view()),

]
