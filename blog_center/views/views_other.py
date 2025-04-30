from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(reqeust):
    return render(reqeust, 'dashboard/dash.html')
