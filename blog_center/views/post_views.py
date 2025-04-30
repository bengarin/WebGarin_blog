from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_center.models import Category

def post_create(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'posts/create_posts.html',context)