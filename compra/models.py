from django.db import models
from django.utils import timezone
from inventario.models import Colore, Estampado, Prenda, Talla
from registro.models import Usuario


class Personalizada(models.Model):
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    color = models.ForeignKey(Colore, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    estampado = models.ForeignKey(Estampado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    fabricada = models.BooleanField()
    entregada = models.BooleanField()
    carrito = models.BooleanField()
    pagado = models.BooleanField()


    def __str__(self):
        return self.prenda
