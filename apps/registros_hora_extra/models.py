from django.db import models

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.motivo
