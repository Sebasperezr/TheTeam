from django.shortcuts import render
from rest_framework import viewsets
from .models import Empresa
from .serializador import EmpresaSerializador


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class =EmpresaSerializador
    queryset = Empresa.objects.all()