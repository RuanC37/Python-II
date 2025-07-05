from django.db import models
from datetime import datetime
from funcionario.models import Funcionario
# Create your models here.

class Prato(models.Model):
    nome_prato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.CharField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=10)
    categoria = models.CharField(max_length=100)
    date_prato = models.DateTimeField(default=datetime.now, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)
    foto_prato = models.ImageField(upload_to='pratos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.nome_prato
    
