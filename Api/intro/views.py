from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import intro
from .serializer import introSerializer

@api_view(['GET'])
def get_intro(request):
    return Response(introSerializer({'name': "mahanthi", "age": 25}).data)

@api_view(['POST'])
def post_intro(request):
    serializer = introSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

