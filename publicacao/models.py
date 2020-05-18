from django.db import models
from datetime import datetime #importa o modulo de tempo do Django
from django.contrib.auth.models import User
from user.models import Usuario

class Publicacao(models.Model):
    usuario = models.ForeingKey(Usuario, on_delete.CASCADE)
    nome_publicacao = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    preco = models.FloatField()
    data_publicacao = models.DateField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_publicacao = models.ImageField(upload_to='fotos/%d/%m/%Y', blank = True)

    def __str__(self):
        return "Nome do objeto é = %s" % self.foto_publicacao


 class Comentario(models.Model):
     #relacionamento 1:n
     publicacao = models.ForeingKey(Publicacao, on_delete.CASCADE)
     usuario = models.ForeingKey(Usuario, on_delete.CASCADE)
     titulo = models.CharField(max_length=100)
     descricao = models.TextField()
