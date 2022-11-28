from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import render
# Create your views here.

def login(request):
    cc="<h1>homee</h1>"
    return render(request,'login/login.html')