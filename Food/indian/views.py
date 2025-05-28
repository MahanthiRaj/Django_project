from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages

def andhra(request):
    return HttpResponse("The list of Andhra Dishes")
def tamil(request):
    return HttpResponse("The list of tamil Dishes")
def northindian(request):
    return HttpResponse("The list of North indian Dishes")
def Indiancuisine(request):
    return render(request,'indian.html')


    

def login_view(request):
    if request.method == 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')
     user = authenticate(request, username = username,password = password)
     if user:
         login(request, user)
         return redirect("indian")
     else:
        messages.error(request, "Invalid username and password, please sign up")
        return redirect("signup")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user.object.filter(username = username, password = password):
            messages.erroe(request, "username already exixts.")
            return redirect('login')
        user.object.create_user(username = username, password = password)
        messages.success(request, "sign up successful, Now you can login")
        return redirect('login')
    return render(request,'sign.html')

