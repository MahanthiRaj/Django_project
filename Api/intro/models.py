from django.db import models

class intro(models.Model):
    
    age = models.IntegerField()
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name 
    
print(intro)

# Create your models here.
