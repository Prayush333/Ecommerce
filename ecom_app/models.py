from django.db import models
import datetime

class Catagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=3, max_digits=8)
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE, default =1 )
    

class Order(models.Model):
    pass
