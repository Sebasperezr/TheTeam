from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    contraseña = models.CharField(max_length = 100)
    idEmpresa = models.CharField(max_length = 100)

    def __str__(self):
        return self.pk