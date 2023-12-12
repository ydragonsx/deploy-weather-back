from django.db import models

from usuario.models import Usuario

class FavotiteCity(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    
