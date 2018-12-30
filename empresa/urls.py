from django.urls import path
from empresa import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.empresaView),
    path('empresa/<int:pk>', views.empresa_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)