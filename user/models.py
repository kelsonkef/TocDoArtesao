from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneFiled(User, on_delete=models.CASCADE)
    nome = models.CharFild(max_legth=200)
    data_nascimento = models.DateField(blank=true)
    estado = models.CharFild(max_legth=30)
    cidade = models.CharFild(max_legth=100)
    email = models.CharFild(max_legth=100)
    telefone= models.CharFild(max_legth=20, blank=true)
