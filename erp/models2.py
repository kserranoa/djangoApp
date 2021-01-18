from django.db import models
from datetime import datetime

class Empleado(models.Model):
    nombre = models.TextField()
    cedula = models.CharField(max_length=11)
    fecha_ingreso = models.DateField(default=datetime.now)
    fotoPasaporte = models.ImageField(upload_to='foto%Y%m%d')
    salario = models.DecimalField(decimal_places=2, max_digits=9, default=0.00)
    curriculum = models.FileField(upload_to='cv%Y%m%d')
    estado = models.BooleanField(default=True)
    edad = models.PositiveIntegerField()
