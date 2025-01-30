# Aqui Serializers convertem as instâncias de modelos Django em formtos como JSON, facilitando a criação de APIs.

from django.db import models

class holiday(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    tipo = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} em {self.data}"