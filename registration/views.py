
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')
def leaderboard(request):
    return render(request,'leaderboard.html')
def logout(request):
    logout(request)
    return render(request,'login.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm pasword are not same ")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('user_created')
            print(uname,pass1)

    return render(request, 'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username, password=pass1)
        print(username,pass1)
        if user is not None:
            login(request,)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')
def user_created(request):
    
    return render(request,'user_created.html')
    
def portfoliostock(request):
    url = 'https://retoolapi.dev/Rvc0r1/nifty50data'
    r = requests.get(url)
    data = r.json()

    print(data)
    response=requests.get(data)
    return render(request, 'home.html',{'response':response})


