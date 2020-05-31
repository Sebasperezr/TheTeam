from rest_framework import serializers
from .models import rol


class RolSerializador(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'