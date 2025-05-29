from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def Indiancuisine(request):
    template = loader.get_template('indian.html')
    return HttpResponse(template.render())

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
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print("Username:", username) 

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('indian')
    return render(request, 'signup.html')


def home(request):
    return render(request, 'index.html')

def andhra(request):
    return render(request, 'andhra.html')

def tamil(request):
    return render(request, 'tamil.html')

def northindian(request):
    return render(request, 'north.html')