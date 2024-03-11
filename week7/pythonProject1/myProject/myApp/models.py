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


class Category(models.Model):
    name = models.CharField(max_length= 100)
    visits = models.IntegerField()
    likes = models.IntegerField()

class Page(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    url = models.URLField()
    views = models.IntegerField()


class Human(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    