from django.db import models
from apps.empresas.models import Empresa
from django.shortcuts import reverse



class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    
    def get_absolute_url(self):
        return reverse('list_departamentos')
    
    def __str__(self):
        return self.nome