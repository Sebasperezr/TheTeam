from django.db import models


class Empresa(models.Model):
        idEmpresa = models.CharField(max_length = 100)
        Nombre = models.CharField(max_length = 100)


        def __str__(self):
            return self.pk