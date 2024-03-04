from django.db import models

# Create your models here.
class Works(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    
class Lives(models.Model):
    name = models.CharField(max_length= 100)
    street = models.CharField(max_length= 100)
    city = models.CharField(max_length= 100)

class Product(models.Model):
    title = models.CharField(max_length= 100)
    price = models.IntegerField()
    description = models.CharField(max_length = 1000)
    