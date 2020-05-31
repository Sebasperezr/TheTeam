from django.db import models

class Actividad(models.Model):
        tipo = models.CharField(max_length = 100)


        def __str__(self):
            return self.pk
