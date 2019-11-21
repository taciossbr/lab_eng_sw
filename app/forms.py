from django import forms
from django.contrib.auth.models import User
from .models import Pedido, Cliente, Funcionario


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = (
            'id',
            'status',
            'modelo_carro',
            'cliente',
            'concessionaria',
            'status_pagamento',
            'forma_pagamento',
            'protocolo_montadora',
            'dt_pedido',
            'dt_entrega',
            'dt_retirada',
        )
        widgets = {
            'dt_pedido': forms.DateTimeInput(),
            'dt_entrega': forms.DateTimeInput(),
            'dt_retirada': forms.DateTimeInput(),
            'id': forms.TextInput(attrs={'disabled': True}),
            'modelo_carro': forms.TextInput(attrs={'disabled': True}),
            'cliente': forms.Select(attrs={'disabled': True}),
            'concessionaria': forms.TextInput(attrs={'disabled': True}),
            # 'status': forms.Select(attrs={'disabled': True}),
            'forma_pagamento': forms.Select(attrs={'disabled': True}),
            'protocolo_montadora': forms.TextInput(attrs={'disabled': True}),
        }

class ReadOnlyPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = (
            'id',
            'status',
            'modelo_carro',
            'cliente',
            'concessionaria',
            'status_pagamento',
            'forma_pagamento',
            'protocolo_montadora',
            'dt_pedido',
            'dt_entrega',
            'dt_retirada',
        )
        widgets = {
            'dt_pedido': forms.DateTimeInput(attrs={'disabled': True}),
            'dt_entrega': forms.DateTimeInput(attrs={'disabled': True}),
            'dt_retirada': forms.DateTimeInput(attrs={'disabled': True}),
            'id': forms.TextInput(attrs={'disabled': True}),
            'modelo_carro': forms.TextInput(attrs={'disabled': True}),
            'cliente': forms.Select(attrs={'disabled': True}),
            'concessionaria': forms.TextInput(attrs={'disabled': True}),
            # 'status': forms.Select(attrs={'disabled': True}),
            'forma_pagamento': forms.Select(attrs={'disabled': True}),
            'protocolo_montadora': forms.TextInput(attrs={'disabled': True}),
            'status': forms.Select(attrs={'disabled': True}),
            'status_pagamento': forms.Select(attrs={'disabled': True}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'password'
        )
        widgets = {
            'is_staff': forms.HiddenInput(),
            'password': forms.PasswordInput(),
        }


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = (
            'concessionaria',
        )
        # widgets = {
        #     'user': UserForm()
        # }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'cpf',
            'nome',
            'email',
            'telefone',
            'endereco',
            'cnh',
        )
        widgets = {
            'cpf': forms.TextInput(attrs={'readonly': True}),
        }