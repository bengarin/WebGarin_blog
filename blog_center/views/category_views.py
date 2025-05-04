from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_center.models import Category
from blog_center.forms import CategoryForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def category(request):
    qset = Category.objects.all()
    context = {
        'category_list': qset,
    }
    return render(request, 'category/list_category.html',context)
@login_required

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')   
    else:
        form = CategoryForm()
    context = {
        "form":form,
    }
    return render(request, 'category/create_category.html',context)

@login_required

def category_update(request, id):
    instance =get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=instance)
        if form.is_valid():
            name= form.cleaned_data['name']
            slug = form.cleaned_data['slug']
            status = form.cleaned_data['status']
            icons = form.cleaned_data['icons']
            instance.name= name
            instance.slug= slug
            instance.status= status
            instance.icons= icons 
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    context = {
        "form":form,
        "instance": instance,
    }
    return render(request, 'category/update_category.html' ,context)