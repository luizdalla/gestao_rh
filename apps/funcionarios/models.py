from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome