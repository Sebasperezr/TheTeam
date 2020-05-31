"""Aplicacioees.Usuario Vistas."""
from django.shortcuts import render
from rest_framework import viewsets
from .models import usuario
from .serializador import UsuarioSerializador


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class =UsuarioSerializador
    queryset = usuario.objects.all()



