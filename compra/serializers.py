from .models import Personalizada
from rest_framework import serializers


class PersonalizadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalizada
        fields = '__all__'
