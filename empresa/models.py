from django.db import models

class Empresa(models.Model):
    descripcion = models.TextField()
    composicion = models.TextField()
    correo = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()


    def __str__(self):
        return self.descripcion