from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    nivel = models.IntegerField()

    def __str__(self):
        return self.nombre

