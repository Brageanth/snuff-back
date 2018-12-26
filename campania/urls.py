from django.urls import path
from campania import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.campaniaView),
    path('campania/<int:pk>', views.campania_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)