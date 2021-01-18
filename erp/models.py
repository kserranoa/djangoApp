from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=190, verbose_name='Tipo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'Tipos'
        ordering = ['id']

# Create your models here.
class Employee(models.Model):
    names = models.TextField(verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name= 'Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name= 'fechaRegistro')
    date_created = models.DateTimeField(auto_now=True,verbose_name='fechaCreacion')
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=50)
    salary = models.DecimalField(default=0.00, max_digits= 9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar')
    cvitae = models.FileField(upload_to='cvitae%Y%m%d')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
