from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog_center.forms import AuthForms

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method == 'POST':
        form = AuthForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                return render(request, 'auth/login.html', {
                    'form': form,
                    'error': "Identifiants incorrects."
                })
    else:
        form = AuthForms()

    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('blog_login')  