from django.urls import path
from .views import show_all_cars,search_cars,create_post,remove_post,edit_post, get_posts

urlpatterns = [
    path('all_cars/',show_all_cars.as_view()),
    path('search/',search_cars.as_view()),
    path('create/',create_post.as_view()),
    path('remove/',remove_post.as_view()),
    path('edit/',edit_post.as_view()),
    path('get_posts/',get_posts.as_view()),
]