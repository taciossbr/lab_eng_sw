from django import forms
from .models import Pedido, Cliente


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
        }

