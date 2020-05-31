from django.db import models

class Encuesta(models.Model):
        fecha = models.DateTimeField(max_length = 100)
        idActividad = models.CharField(max_length = 100)
        idUsuario = models.CharField(max_length = 100)
        fecha_Baja = models.DateTimeField(max_length = 100)
        idActividad = models.CharField(max_length = 100)
        idRespuesta = models.CharField(max_length = 100 )
        idResultado = models.CharField(max_length = 100, blank = True, null = True )
        audio = models.FileField(max_length = 100, blank = True, null = True, default='' )
        
        def __str__(self):
            return self.pk
        
        



