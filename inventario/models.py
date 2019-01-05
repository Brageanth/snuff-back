from django.db import models
from django.utils import timezone


class Prenda(models.Model):
    CAMIBUSO = 'CB'
    CHAQUETA = 'CH'
    CHAQUETACAPOTA = 'CHC'
    CAMISETA = 'C'
    BUSOCAPOTA = 'BC'
    TIPO_CHOICES = (
        (CAMIBUSO, 'Camibuso'),
        (CHAQUETA, 'Chaqueta'),
        (CHAQUETACAPOTA, 'Chaqueta con capota'),
        (CAMISETA, 'Camiseta'),
        (BUSOCAPOTA, 'Buso con capota'),
    )
    tipo = models.CharField(
        max_length=2,
        choices=TIPO_CHOICES,
        default=CHAQUETA,
    )
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.ImageField()


    def __str__(self):
        return self.tipo


class Colore(models.Model):
    color = models.CharField(max_length=50)
    hexadecimal = models.CharField(max_length=7)
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    imagen = models.ImageField()

    def __str__(self):
        return self.color


class Talla(models.Model):
    S = 'S'
    M = 'M'
    L = 'L'
    TALLA_CHOICES = (
        (S, 'S'),
        (M, 'M'),
        (L, 'L'),
    )
    talla = models.CharField(
        max_length=2,
        choices=TALLA_CHOICES,
        default=M,
    )
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    color = models.ForeignKey(Colore, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.prenda.tipo

class Estampado(models.Model):
    CINESERIES = 'CS'
    ARTE = 'A'
    MUSICA = 'M'
    CATEGORIA_CHOICES = (
        (CINESERIES, 'Cine y series'),
        (ARTE, 'Arte'),
        (MUSICA, 'Musica'),
    )
    nombre = models.CharField(max_length=100, primary_key=True)
    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIA_CHOICES,
        default=CINESERIES,
    )
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    color = models.ForeignKey(Colore, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    stock = models.BooleanField()
    imagenPrenda = models.ImageField()
    imagenEstampado = models.ImageField()
    imagenPreview = models.ImageField()

    def __str__(self):
        return self.nombre
