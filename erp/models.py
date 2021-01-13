from django.db import models

# Create your models here.
class Employee(models.Model):
    names = models.TextField(verbose_name='Nombres')
    
