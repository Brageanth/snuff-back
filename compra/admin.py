from django.contrib import admin
from .models import Personalizada

class PersonalizadaAdmin(admin.ModelAdmin):
    list_display = ('prenda', 'estampado', 'usuario', 'fabricada', 'entregada', 'pagada', 'precio_total')
    search_fields = ('usuario')

admin.site.register(Personalizada, PersonalizadaAdmin)
