from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
# If any of user directly want to access the index.html page then he cannot enter directly to the home page without login
@login_required(login_url='login')

def index(request):
    return render(request,"index.html")


def signup(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if(password == cpassword):
            user = User.objects.create_user(name,email,password)
            user.save()
            return redirect('login')
        else:
            return HttpResponse("The password and Confirm Password Didn;t match")
        
    return render(request,"signup.html")

def Login(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        password=request.POST.get("password")
        user = authenticate(request,username=name, password=password)
        print(name,password)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("The username and password didn't match")
        
    return render(request,"login.html")


def Logout(request):
    logout(request)
    return redirect("login")
    
