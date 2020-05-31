from rest_framework import serializers
from .models import Encuesta


class EncuestaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'