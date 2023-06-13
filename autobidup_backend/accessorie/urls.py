from django.urls import path
<<<<<<< HEAD
from .views import show_all_products, search_products, place_order,product_type

=======
from .views import show_all_products, search_products, place_order, CancelOrder
# from django.conf import settings
# from django.conf.urls.static import static
>>>>>>> be6e4767fc1417d815c4611c4f14196369d41af5
urlpatterns = [
    path('all_products/',show_all_products.as_view()),
    path('search/',search_products.as_view()),
    path('order/',place_order.as_view()),
<<<<<<< HEAD
    path('product_type/',product_type.as_view()),

=======
    path('cancel/<str:order_id>/',CancelOrder.as_view()),
>>>>>>> be6e4767fc1417d815c4611c4f14196369d41af5
]