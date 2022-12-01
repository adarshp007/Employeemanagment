from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import json

from django.shortcuts import render
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from rest_framework import generics,status
from employee.models import User
from employee.serializers import (UserSerializers)
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView
from rest_framework import status

def register_view(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        usercount=User.objects.filter(email=email).count()
        if usercount >0:
            messages.success(request,"User already exist")
            return redirect('register'
            )
        try:    
            user=User.objects.create(email=email,username=email)
            user.set_password(password)
            user.user_type=1
            user.save()
            return redirect('login')
        except Exception as e:
            messages.success(request,e)
    return render(request,'register/register.html')

@login_required(login_url='/login/')
def employee_view(request):
    
    if request.method=="POST":
        user=User.objects.get(id=request.POST['usrid'])
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        # user.email=request.POST['email']
        user.mobile=request.POST['phone']
        user.date_of_birth=request.POST['dob']
        user.salary=request.POST['salary']
        user.save()
    queryset=User.objects.filter(user_type=0).order_by('first_name')
    serializer=UserSerializers(queryset,many=True)
    context=serializer.data
    return render(request,'employees/employees.html',{"employees":context})

@login_required(login_url='/login/')
def salary_view(request):
    # import pdb;pdb.set_trace();
    empid=request.session['empid']
    user=User.objects.get(id=empid)
    serializer=UserSerializers(user)
    context=serializer.data
    if request.method=="POST":
        
        try:
            user.salary=request.POST["salary"]
            user.save()
        except Exception as e:
            messages.success(request,e)

            return redirect("salary")
        return redirect('employees')
    return render(request,'salary/salary.html',context)
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    if request.method== "POST":
        
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        employeecode=request.POST['employee_code']
        dateofbirth=request.POST['dob']
        phone=request.POST['phone']
        # import pdb;pdb.set_trace();
        
        useremailcount=User.objects.filter(email=email).count()
        
        if useremailcount >0:
            messages.success(request,f"Employee {email} already exist")
            return redirect('index')
        try:
            # import pdb;pdb.set_trace();

            user=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=email,mobile=phone,employee_code=employeecode,date_of_birth=dateofbirth)
            request.session['empid']=request.session.get('empid',0)
            del request.session['empid']
            request.session['empid']=user.id
            
        except Exception as e:
            messages.success(request,e)
            return redirect('index')

        
        return redirect('salary')
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
            return redirect('index')
        else:
            messages.success(request,"Incorrect email or password please try again")
            return redirect('login')
    else:
        return render(request,'login/login.html')

def logout_view(request):

    logout(request)
    return redirect('login')




class Employees(generics.CreateAPIView):   
    serializer_class = UserSerializers
    http_method_names = ['get']
    

    def get(self,request,*args,**kwargs):
        queryset=User.objects.filter(user_type=0)
        
        serializer=UserSerializers(queryset,many=True)
        
        return Response(serializer.data,status.HTTP_200_OK)     


class UserDetails(generics.CreateAPIView):
    serializer_class = UserSerializers
    http_method_names = ['get']
    queryset=User.objects.all()

    def get(self,*args,**kwargs):
        

        queryset=User.objects.get(id=self.kwargs['userid'])
        serializer=UserSerializers(queryset)
        return Response(serializer.data,status.HTTP_200_OK)
    
    
    

@login_required(login_url='/login/')  
@csrf_exempt
def user_update_view(request):
    if request.method=="POST":
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        return redirect('employees')


def user_delete_view(request):
    if request.method=="POST":
        # import pdb;pdb.set_trace;

        print("shjshjsh")
        return HttpResponse("post req success")

# class UserUpdate(generics.CreateAPIView):
#     serializer_class = UserSerializers
#     http_method_names = ['get']
#     queryset=User.objects.all()

#     def get(self,*args,**kwargs):
#         # import pdb;pdb.set_trace();

#         queryset1=User.objects.filter(id=self.kwargs['userid']).delete()
#         queryset=User.objects.all()
        
#         serializer=UserSerializers(queryset,many=True)
#         return Response(serializer.data,status.HTTP_200_OK)


class UserUpdate(ListView):
    
    def delete(self,*args, **kwargs):
        User.objects.filter(id=self.kwargs['userid']).delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
 