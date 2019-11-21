from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Funcionario, Gerente, Admin

from django.contrib.auth.models import Group

admin_group = Group.objects.get(name='admin')
gerentes_group = Group.objects.get(name='gerentes')
funcionarios_group = Group.objects.get(name='funcionarios')


@receiver(post_save, sender=Funcionario)
def add_funcionario_group(sender, instance, created, **kwargs):
    funcionarios_group.user_set.add(instance.user)


@receiver(post_save, sender=Gerente)
def add_gerente_group(sender, instance, created, **kwargs):
    gerentes_group.user_set.add(instance.user)


@receiver(post_save, sender=Admin)
def add_admin_group(sender, instance, created, **kwargs):
    admin_group.user_set.add(instance.user)
