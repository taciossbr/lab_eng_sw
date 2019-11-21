from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Concessionaria(models.Model):
    endereco = models.CharField(max_length=140)
    cnpj = models.CharField(max_length=20)
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

    def __str__(self):
        return self.nome

AGUARDANDO = 'AG'
ANALISE = 'AN'
ACEITO = 'AC'
RECUSADO = 'RE'

STATUS_PAGAMENTO = (
    (AGUARDANDO, 'AGUARDANDO'),
    (ANALISE, 'ANALISE'),
    (ACEITO, 'ACEITO'),
    (RECUSADO, 'RECUSADO'),
)

CARTAO_CREDITO = 'CC'
CARTAO_DEBITO = 'CD'
BOLETO_BANCARIO = 'BB'
TRANSFERENCIA_BANCARIA = 'TB'
DINHEIRO = 'D'


FORMA_PAGAMENTO = (
    (CARTAO_CREDITO, 'CARTAO CREDITO'),
    (CARTAO_DEBITO, 'CARTAO DEBITO'),
    (BOLETO_BANCARIO, 'BOLETO BANCARIO'),
    (TRANSFERENCIA_BANCARIA, 'TRANSFERENCIA BANCARIA'),
    (DINHEIRO, 'DINHEIRO'),
)

ABERTO = 'AB'
PRODUCAO = 'PD'
EM_TRANSPORTE = 'TP'
ENTREGUE = 'EN'

STATUS_PEDIDO = (
    (ABERTO, 'ABERTO'),
    (PRODUCAO, 'PRODUCAO'),
    # (EM_TRANSPORTE, 'EM TRANSPORTE'),
    # (ENTREGUE, 'ENTREGUE'),
    (AGUARDANDO, 'AGUARDANDO RETIRADA'),
)


class Pedido(models.Model):
    status = models.CharField(
        max_length=15,
        choices=STATUS_PEDIDO,
        default=ABERTO
    )
    modelo_carro = models.CharField(max_length=200)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos')
    concessionaria = models.ForeignKey(
        Concessionaria,
        on_delete=models.CASCADE,
        related_name='pedidos',)
    status_pagamento = models.CharField(
        max_length=15,
        choices=STATUS_PAGAMENTO,
        default=AGUARDANDO
    )
    forma_pagamento = models.CharField(
        max_length=15,
        choices=FORMA_PAGAMENTO,
        default=TRANSFERENCIA_BANCARIA
    )
    protocolo_montadora = models.IntegerField(null=True, blank=True)
    dt_pedido = models.DateTimeField()
    dt_entrega = models.DateTimeField()
    dt_retirada = models.DateTimeField()

class Admin(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

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
