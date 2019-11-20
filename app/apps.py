
from django.apps import AppConfig
# from app.models import Funcionario


class MyAppConfig(AppConfig):
    name = 'app'

    def ready(self):
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        print('oooooooooooooooooooooooooooooooooooooooooooooo')
        # Group = self.get_model('django.contrib.auth.Group')
        # Permission = self.get_model('Permission')
        # ContentType = self.get_model('ContentType')
        add_user = Permission.objects.filter(codename='add_user')[0]
        change_user = Permission.objects.filter(codename='change_user')[0]
        delete_user = Permission.objects.filter(codename='delete_user')[0]
        view_user = Permission.objects.filter(codename='view_user')[0]
        Funcionario = self.get_model('Funcionario')
        Gerente = self.get_model('Gerente')
        ct_funcionario = ContentType.objects.get_for_model(Funcionario)
        
        can_edit_funcionario, _ = Permission.objects.get_or_create(
            codename="can_edit_funcionario",
            content_type=ct_funcionario)
        ct_gerente = ContentType.objects.get_for_model(Gerente)
        can_edit_gerente, _ = Permission.objects.get_or_create(
            codename="can_edit_gerente",
            content_type=ct_gerente)
        print(type(add_user), type(can_edit_funcionario))
        try:
            admin_group, _ = Group.objects.get_or_create(
                name='admin'
            )

            admin_group.permissions.add(can_edit_gerente)
            admin_group.permissions.add(can_edit_funcionario)
            admin_group.permissions.add(add_user)
            admin_group.permissions.add(change_user)
            admin_group.permissions.add(delete_user)
            admin_group.permissions.add(view_user)

        except Exception as e:
            print(e, 'admin')
            
        try:
            
            gerentes_group, _ = Group.objects.get_or_create(
                name='gerentes'
            )
            gerentes_group.permissions.add(can_edit_funcionario)
            gerentes_group.permissions.add(add_user)
            gerentes_group.permissions.add(change_user)
            gerentes_group.permissions.add(delete_user)
            gerentes_group.permissions.add(view_user)
        except Exception as e:
            print(e)
            
        try:
            funcionarios, _ = Group.objects.get_or_create(
                name='funcionarios'
            )
        except Exception as e:
            print(e)
            
        
