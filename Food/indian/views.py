from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def andhra(request):
    return HttpResponse("The list of Andhra Dishes")
def tamil(request):
    return HttpResponse("The list of tamil Dishes")
def northindian(request):
    return HttpResponse("The list of North indian Dishes")
def Indiancuisine(request):
    template = loader.get_template('indian.html')
    return HttpResponse(template.render())


