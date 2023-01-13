from django.db import models

# Create your models here.


class Jugadores(models.Model): 
    name = models.CharField(max_length= 50)
    price = models.FloatField()

class Clubes(models.Model): 
    name = models.CharField(max_length= 50)
    country = models.CharField(max_length= 50)

class Tecnicos(models.Model): 
    name = models.CharField(max_length= 50)
    edad = models.FloatField()
