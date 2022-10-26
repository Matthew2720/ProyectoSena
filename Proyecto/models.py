#from unittest.util import _MAX_LENGTH
from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    edad=models.CharField(max_length=10)
    celular=models.CharField(max_length=15)
    fechanacimiento=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    genero=models.CharField(max_length=100)
    cedula=models.CharField(max_length=20)
    class Meta:
        db_table = 'clientes'