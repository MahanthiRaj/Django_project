from django.urls import path
from .views import get_intro , post_intro

urlpatterns = [
    path('intro/', get_intro, name='get_intro'),
    path('post/', post_intro, name='post_intro') 
]