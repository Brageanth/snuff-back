from .models import Empresa
from rest_framework import serializers, viewsets


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
