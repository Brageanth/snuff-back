from django.urls import path
from inventario import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('/prenda', views.prendaView),
    path('/prenda/<int:pk>', views.prenda_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)
