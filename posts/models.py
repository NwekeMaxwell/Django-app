from django.db import models

# Create your models here.
class Feature(models.Model): #correct way to define a working model 
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

# class Feature:  ----------you can import this to your view and use it as your mock model for your components
#     id: int
#     name: str
#     details: str
