from rest_framework import serializers
from .models import Empresa


class EmpresaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'