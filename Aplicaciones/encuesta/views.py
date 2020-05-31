from django.shortcuts import render
from rest_framework import viewsets
from .models import Encuesta
from .serializador import EncuestaSerializador


class EncuestaViewSet(viewsets.ModelViewSet):
    serializer_class =EncuestaSerializador
    queryset = Encuesta.objects.all()



