from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
import requests
import json

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
        messages.error(request, "Invalid username and password, please verify")
    
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

import requests
from django.shortcuts import render

def andhra(request):
    temp_c = None
    wind_mph = None
    humidity = None
    category = None
    city = ""

    if request.method == "POST":
        city = request.POST.get("city")

        url = f"http://api.weatherapi.com/v1/current.json?key=63696680b70842f6961165644250806&q={city}"

        try:
            response = requests.get(url)
            print("Response Text:", response.text)
            data = response.json()

            temp_c = data["current"]["temp_c"]
            wind_mph = data["current"]["wind_mph"]
            humidity = data["current"]["humidity"]

            if 18 <= temp_c <= 25:
                category = "cold"
            elif 25 < temp_c <= 30:
                category = "sunny"
            elif temp_c > 30:
                category = "hot"

        except Exception as e:
            temp_c = f"Error: {str(e)}"

    context = {
        "temp_c": temp_c,
        "wind_mph": wind_mph,
        "humidity": humidity,
        "category": category,
        "city": city
    }

    return render(request, "andhra.html", context)

def tamil(request):
    temp_c = None
    wind_mph = None
    humidity = None
    category = None
    city = ""

    if request.method == "POST":
        city = request.POST.get("city")

        url = f"http://api.weatherapi.com/v1/current.json?key=63696680b70842f6961165644250806&q={city}"

        try:
            response = requests.get(url)
            print("Response Text:", response.text)
            data = response.json()

            temp_c = data["current"]["temp_c"]
            wind_mph = data["current"]["wind_mph"]
            humidity = data["current"]["humidity"]

            if 18 <= temp_c <= 25:
                category = "cold"
            elif 25 < temp_c <= 30:
                category = "sunny"
            elif temp_c > 30:
                category = "hot"

        except Exception as e:
            temp_c = f"Error: {str(e)}"

    context = {
        "temp_c": temp_c,
        "wind_mph": wind_mph,
        "humidity": humidity,
        "category": category,
        "city": city
    }

    return render(request, "tamil.html", context)
   

def northindian(request):
    temp_c = None
    wind_mph = None
    humidity = None
    category = None
    city = ""

    if request.method == "POST":
        city = request.POST.get("city")

        url = f"http://api.weatherapi.com/v1/current.json?key=63696680b70842f6961165644250806&q={city}"

        try:
            response = requests.get(url)
            print("Response Text:", response.text)
            data = response.json()

            temp_c = data["current"]["temp_c"]
            wind_mph = data["current"]["wind_mph"]
            humidity = data["current"]["humidity"]

            if 18 <= temp_c <= 25:
                category = "cold"
            elif 25 < temp_c <= 30:
                category = "sunny"
            elif temp_c > 30:
                category = "hot"

        except Exception as e:
            temp_c = f"Error: {str(e)}"

    context = {
        "temp_c": temp_c,
        "wind_mph": wind_mph,
        "humidity": humidity,
        "category": category,
        "city": city
    }

    return render(request, "north.html", context)
   



