from django.urls import path
from .views import show_all_products, search_products, place_order, CancelOrder
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('all_products/',show_all_products.as_view()),
    path('search/',search_products.as_view()),
    path('order/',place_order.as_view()),
    path('cancel/<str:order_id>/',CancelOrder.as_view()),
]