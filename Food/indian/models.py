from django.db import models

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
  
class cities(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name