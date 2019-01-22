from .models import Usuario, UsuarioReset
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioReset
        fields = ('correo',)
