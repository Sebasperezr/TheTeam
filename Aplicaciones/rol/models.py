from django.db import models

class rol(models.Model):
        descripcion = models.TextField(max_length = 100)


        def __str__(self):
            return self.pk
