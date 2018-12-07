from .models import Prenda, Colore, Talla, Estampado
from rest_framework import serializers


class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenda
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colore
        fields = '__all__'


class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talla
        fields = '__all__'


class EstampadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estampado
        fields = '__all__'
