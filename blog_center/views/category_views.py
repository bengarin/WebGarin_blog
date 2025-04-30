from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_center.models import Category

def category(request):
    qset = Category.objects.all()
    context = {
        'category_list': qset,
    }
    return render(request, 'category/list_category.html',context)