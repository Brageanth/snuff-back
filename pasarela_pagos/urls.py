from django.urls import path
from pasarela_bancos import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.consulta_bancos),
]


urlpatterns = format_suffix_patterns(urlpatterns)