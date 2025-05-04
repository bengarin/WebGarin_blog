from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # posts
    path("post/",views.post,name='post'),
    path('posts/create/',views.post_create,name='post_create'),
    # category
    path('category/',views.category,name='category'),
    path('category/create/',views.category_create,name='category_create'),
    path('category/update/<int:id>',views.category_update,name='category_update'),
    # auth
    path('login/',views.login_view,name='blog_login'),
    path('logout/',views.logout_view,name='blog_logout'),
]
