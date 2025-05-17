# Django_project# Django

Mahanthi: creating a repo, created a database and a html page

pranay: created a logic in urls.py and views.py, configuring in settings.py

step-1 :created a repository named  Django_project

step-2: created a virtual environment using the following command

          python -m venv env
          
step-3: activates the environment

          .env\Scripts\activate
step-4: after activation ,Installed Django

          pip install django
step-5: created a Django project - Food

          django-admin startproject Food
step-6: under Health project created a subapp - indian:

          python manage.py startapp indian
step-7: Create Views in views.py

            from django.shortcuts import render
            from django.http import HttpResponse
            from django.template import loader

            def andhra(request):
                return HttpResponse("The list of Andhra Dishes")
            def tamil(request):
                return HttpResponse("The list of tamil Dishes")
            def northindian(request):
                return HttpResponse("The list of North indian Dishes")

step-8: created a urls.py file inside the indian app and added the URL patterns 

                urlpatterns = [
            path('andhra/',andhra, name ='andhra'),
            path('tamil/',tamil, name ='tamil'),
            path('north/',northindian, name ='north-indian'),
            path('cuisine/',Indiancuisine, name ='Indian-cuisine')
        ]

step-9: added the Indian app URLs in the main project- Food->urls.py

            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('indian.urls'))
            ]


step-10: Finally i ran the server to test the project locally

            python manage.py runserver

            http://127.0.0.1:8000/indian/
step-11: created an HTML template under indian
step-12: created a view function that renders an HTML page using Django -> template.loader

            from django.template import loader

            def Indiancuisine(request):
            template = loader.get_template('indian.html')
            return HttpResponse(template.render())


step -12: Then connected the Indiancuisine view to a URL to get access the browser 

          from patients.views import Indiancuisine
          from django.urls import path
          
          urlpatterns = [
                      path('cuisine/',Indiancuisine, name='Indian-cuisine'),
                    
          ] 
setp-13: Then we run the server to check the expected output
step-14: created models in Django to store information about andhra, tamil and northindian in the database. 
         
          
            class andhra(models.Model):
                dishname = models.CharField(max_length = 255)
                masalaused= models.CharField(max_length = 255)
                vegitablesused = models.CharField(max_length = 255)  
                
            class tamil(models.Model):
                dishname = models.CharField(max_length = 255)
                masalaused= models.CharField(max_length = 255)
                vegitablesused = models.CharField(max_length = 255)  
                
            class northindian(models.Model):
                dishname = models.CharField(max_length = 255)
                masalaused= models.CharField(max_length = 255)
                vegitablesused = models.CharField(max_length = 255)  

step-15:Then we run this command 

          python manage.py makemigrations


step-16: Finally Django will check the models and it will create migration file 
