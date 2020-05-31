from django.shortcuts import render
from rest_framework import viewsets
from .models import rol
from .serializador import RolSerializador


class RolViewSet(viewsets.ModelViewSet):
    serializer_class =RolSerializador
    queryset = rol.objects.all()
