from django.urls import path
from inventario import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('prenda', views.prendaView),
    path('prenda/<int:pk>', views.prenda_detail),
    path('color', views.colorView),
    path('color/<int:pk>', views.color_detail),
    path('talla', views.tallaView),
    path('talla/<int:pk>', views.talla_detail),
    path('estampado', views.estampadoView),
    path('estampado/<int:pk>', views.estampado_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)
