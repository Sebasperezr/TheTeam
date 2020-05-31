from rest_framework import serializers
from .models import usuario


class UsuarioSerializador(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'