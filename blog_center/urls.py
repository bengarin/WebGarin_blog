from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # posts
    path('posts/create/',views.post_create,name='post_create'),
    # category
    path('category/create/',views.category,name='category_create'),
]
