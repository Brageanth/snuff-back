from django.db import models

class Empresa(models.Model):
    descripcion = models.TextField()
    composicion = models.TextField()
    correo = models.CharField(max_length=100)
    telefono = models.BigIntegerField()


    def __str__(self):
        return self.descripcion