from django.db import models
import datetime

class Catagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    pass


    
