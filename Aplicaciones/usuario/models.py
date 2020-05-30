from django.db import models

class usuario(models.Model):
    id = models.CharField(primary_Key =  True)
    nombre = models.CharField(max_length = 100)
    contraseña = models.CharField(max_length = 100)
    idEmpresa = models.CharField(max_length = 100)

 
