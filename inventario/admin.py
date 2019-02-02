from django.contrib import admin
from .models import Prenda, Colore, Talla, Estampado

class EstampadoAdmin(admin.ModelAdmin):
    list_display = ('prenda', 'nombre', 'categoria', 'cantidad', 'stock')
    search_fields = ('nombre',)

admin.site.register(Prenda)
admin.site.register(Colore)
admin.site.register(Talla)
admin.site.register(Estampado, EstampadoAdmin)
