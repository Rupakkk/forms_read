
from django.db import models

# Create your models here.
class FormModel(models.Model):
    name = models.CharField(max_length=50,default='Ram')
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    address = models.CharField(max_length=50)