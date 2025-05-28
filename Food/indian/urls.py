from indian.views import andhra
from indian.views import tamil
from indian.views import login_view
from indian.views import signup
from indian.views import northindian
from indian.views import Indiancuisine
from django.urls import path

urlpatterns = [
    path('signup/', signup, name='Signup'),
    path('andhra/',andhra, name ='andhra'),
    path('tamil/',tamil, name ='tamil'),
    path('north/',northindian, name ='north'),
    path('cuisine/',Indiancuisine, name ='Indian-cuisine'),
    path('login/', login_view, name = 'Login'),
    path('signup/',signup, name = 'Signup')
]
