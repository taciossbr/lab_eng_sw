import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Gerente, Funcionario, Concessionaria, Cliente, Pedido, PRODUCAO
from concessionaria.settings import BASE_MONTADORA
from .forms import PedidoForm
from .serializers import PedidoSerializer, ClienteSerializer, ConcessionariaSerializer


def login_success(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    # is_admin = 'admin' in [group.name for group in user.groups.all()]
    print([group.name for group in user.groups.all()])

    if user.is_staff:
        return redirect('/admin')
    return redirect('/')


def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    is_admin = 'admin' in [group.name for group in user.groups.all()] or user.is_staff
    is_gerente = 'gerentes' in [group.name for group in user.groups.all()]
    is_funcionario = 'funcionarios' in [group.name for group in user.groups.all()]
    user_role = next(filter(lambda el: el[0],
                            zip([is_admin, is_gerente, is_funcionario],
                                ['admin', 'gerente', 'funcionario'])))[1]
    concessionarias = None
    if is_admin:
        concessionarias = Concessionaria.objects.all()
    elif is_gerente:
        gerente = Gerente.objecs.filter(user=user)[0]
        concessionarias = [gerente.concessionaria]
    elif is_funcionario:
        funcionario = Funcionario.objects.filter(user=user)[0]
        concessionarias = [funcionario.concessionaria]

    return render(request, 'home.html', {
            'site_header': 'Concessionarias',
            'user_role': user_role,
            'concessionarias': concessionarias
        })


def concessionaria(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    groups = [group.name for group in user.groups.all()]
    is_admin = 'admin' in [group.name for group in user.groups.all()] or user.is_staff
    is_gerente = 'gerentes' in [group.name for group in user.groups.all()]
    is_funcionario = 'funcionarios' in [group.name for group in user.groups.all()]
    user_role = next(filter(lambda el: el[0],
                            zip([is_admin, is_gerente, is_funcionario],
                                ['admin', 'gerente', 'funcionario'])))[1]
    concessionaria = Concessionaria.objects.get(pk=id)
    funcionarios = concessionaria.funcionarios.all()
    pedidos = concessionaria.pedidos.all()
    return render(request, 'concessionaria.html', {
            'site_header': 'Concessionarias',
            'user_role': user_role,
            'concessionaria': concessionaria,
            'funcionarios': funcionarios,
            'pedidos': pedidos,
        })

def pedido(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    is_admin = 'admin' in [group.name for group in user.groups.all()] or user.is_staff
    is_gerente = 'gerentes' in [group.name for group in user.groups.all()]
    is_funcionario = 'funcionarios' in [group.name for group in user.groups.all()]
    user_role = next(filter(lambda el: el[0],
                            zip([is_admin, is_gerente, is_funcionario],
                                ['admin', 'gerente', 'funcionario'])))[1]
    pedido = Pedido.objects.get(pk=id)
    form = PedidoForm(request.POST or None, instance=pedido)
    # montadora_info = {
    #     "protocolo": 1,
    #     "data_pedido": "2019-11-19T14:32:59.291Z",
    #     "carro_id": 1,
    #     "cnpj": "1238128321",
    #     "email": "alalal@alalala",
    #     "status": "Requisitado",
    #     "id": 1,
    #     "modelo": "Taycan",
    #     "ano": 2020,
    #     "potencia": "100",
    #     "aceleracao": "5,3",
    #     "vel_maxima": "330",
    #     "tracao": "Dianteira",
    #     "preco": "330000.00",
    #     "cor": None
    # }
    montadora_info = None
    try:
        montadora_info = requests.get(
            f'{BASE_MONTADORA}/pedidos/{pedido.protocolo_montadora}',
            timeout=1
        )
    except:
        ...
    if request.method == "POST":
        sen = pedido.status != PRODUCAO and request.POST['status'] == PRODUCAO
        pedido.status = request.POST['status']
        pedido.status_pagamento = request.POST['status_pagamento']
        pedido.save()
        print(sen)
        if sen:
            return redirect(f'/pedido-update/{pedido.id}/1')
            print(f'/pedido-update/{pedido.id}/1')
        else:
            return redirect(f'/pedido-update/{pedido.id}/0')
            print(f'/pedido-update/{pedido.id}/0')
    return render(request, 'pedido.html', {
        'site_header': 'Concessionarias',
        'user_role': user_role,
        'pedido': pedido,
        'form': form,
        'montadora_info': montadora_info
    })

def pedidos_update(request, id, vai):
    pedido = Pedido.objects.get(pk=id)
    # if pedido.
    print(bool(vai), 'vai')
    if vai:
        try:
            resp = requests.post(
                f'{BASE_MONTADORA}/pedidos', 
                {
                    "carro_id": pedido.modelo_carro,
                    "cnpj": pedido.concessionaria.cnpj,
                    "email": pedido.concessionaria.email
                },
                timeout=3
            )
            data = resp.json()
            protocolo = data['protocolo']
            pedido.protocolo_montadora = protocolo
        except:
            ...
    return redirect(f'/pedido/{pedido.id}')


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ConcessionariaViewSet(viewsets.ModelViewSet):
    queryset = Concessionaria.objects.all()
    serializer_class = ConcessionariaSerializer
