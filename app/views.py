from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gerente, Funcionario, Concessionaria, Cliente, Pedido


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
    ...