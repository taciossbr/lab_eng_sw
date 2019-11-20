from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Concessionaria(models.Model):
    endereco = models.CharField(max_length=140)
    status = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    horario_funcionamento = models.CharField(max_length=25)
    email = models.CharField(max_length=120)


class Cliente(models.Model):
    cpf = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=140)
    cnh = models.CharField(max_length=20)
    

class Pedido(models.Model):
    status = models.CharField(max_length=15)
    modelo_carro = models.CharField(max_length=200)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos')
    status_pagamento = models.CharField(max_length=15)
    forma_pagamento = models.CharField(max_length=15)
    dt_pedido = models.DateTimeField()
    dt_entrega = models.DateTimeField()
    dt_retirada = models.DateTimeField()

# class Admin(models.Model):
#     nome = models.CharField(max_length=50)
#     email = models.CharField(max_length=120)

class Gerente(models.Model):
    # nome = models.CharField(max_length=50)
    # email = models.CharField(max_length=120)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    concessionaria = models.ForeignKey(
        Concessionaria,
        on_delete=models.CASCADE,
        related_name='gerentes')


class Funcionario(models.Model):
    # nome = models.CharField(max_length=50)
    # email = models.CharField(max_length=120)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    concessionaria = models.ForeignKey(
        Concessionaria,
        on_delete=models.CASCADE,
        related_name='funcionarios')
