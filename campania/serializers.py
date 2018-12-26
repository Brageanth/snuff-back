from .models import Campania
from rest_framework import serializers, viewsets


class CampaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campania
        fields = '__all__'
