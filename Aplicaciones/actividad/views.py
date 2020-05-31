from django.shortcuts import render
from rest_framework import viewsets
from .models import Actividad
from .serializador import ActividadSerializador


class ActividadViewSet(viewsets.ModelViewSet):
    serializer_class =ActividadSerializador
    queryset = Actividad.objects.all()