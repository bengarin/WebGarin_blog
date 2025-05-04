from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_center.models import Category
from django.contrib.auth.decorators import login_required

@login_required
def post (request):
    qset = Category.objects.all()
    context = {
        'category_list': qset,
    }
    return render(request, 'posts/list_posts.html',context)
@login_required

def post_create(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'posts/create_posts.html',context)