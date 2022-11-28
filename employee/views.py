from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.shortcuts import render
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
# Create your views here.
def home_view(request):
    
    return render(request,'home/home.html')


def login_view(request):
    print(request.method)
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=request.POST['email'], password=request.POST['password'])
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            messages.success(request,"There was a error while logging in please try again...")
            return redirect('login')
    else:
        return render(request,'login/login.html')

def logout_view(request):

    logout(request)
    return redirect('login')


def employees_details_view(request):
    return redirect('login')
 