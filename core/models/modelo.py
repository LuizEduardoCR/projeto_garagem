from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True )
    
    def __str__ (self):
        if self.marca:
            return f'{self.id} {self.marca.upper()} {self.nome.upper()} '
        else:
            return f'{self.id} {self.nome.upper()}'
    