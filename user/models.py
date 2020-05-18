from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    #Relacinamento 1:1
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=True)
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone= models.CharField(max_length=20, blank=True)
