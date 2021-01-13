from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    names = models.TextField(verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name= 'Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name= 'fechaRegistro')
    date_created = models.DateTimeField(auto_now=True,verbose_name='fechaCreacion')
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits= 9, decimal_places=2)
