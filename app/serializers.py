# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pedido, Concessionaria, Cliente

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        # fields = ['url', 'username', 'email', 'groups']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConcessionariaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concessionaria
        fields = '__all__'
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']