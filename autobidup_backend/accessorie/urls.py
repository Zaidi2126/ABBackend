from django.urls import path
from .views import show_all_products, search_products, place_order,CancelOrder, search_product_type

urlpatterns = [
    path('all_products/',show_all_products.as_view()),
    path('search/',search_products.as_view()),
    path('order/',place_order.as_view()),
    path('product_type/',search_product_type.as_view()),
    path('cancel/<str:order_id>/',CancelOrder.as_view()),

]