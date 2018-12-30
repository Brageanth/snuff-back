from django.db import models

class Campania(models.Model):
    copy = models.CharField(max_length=100)
    video = models.FileField()
    descripcion = models.CharField(max_length=250)


    def __str__(self):
        return self.copy