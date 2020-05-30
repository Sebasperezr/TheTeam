from django.db import models

class Encuesta(models.Model)
        id = models.CharField(primary_Key =  True)
        fecha = models.DateTimeField(max_length = 100)
        idActividad = models.CharField(max_length = 100)
        fecha_Baja = models.DateTimeField(max_length = 100)
        idActividad = models.CharField(max_length = 100)
        idRespuesta = models.CharField(max_length = 100)
        idResultado = models.CharField(max_length = 100)
        



