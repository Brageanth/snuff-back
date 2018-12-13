from django.urls import path
from registro import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.usuarioView),
    path('<int:pk>', views.usuario_detail),
    path('reset', views.resetPassword),
    path('resetPassword<int:pk>', views.usuario_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)
