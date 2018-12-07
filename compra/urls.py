from django.urls import path
from compra import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.personalizadaView),
    path('<int:pk>', views.personalizada_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)
