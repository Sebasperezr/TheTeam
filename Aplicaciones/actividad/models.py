from django.db import models

class Actividad(models.Model)
        id = models.CharField(primary_Key =  True)
        tipo = models.CharField(max_length = 100)
