from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    correo = models.EmailField()
    contrasenia = models.CharField(max_length=100)
    celular = models.BigIntegerField()
    direccion = models.CharField(max_length=100)


    def __str__(self):
        return self.correo
