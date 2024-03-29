# Generated by Django 2.2.7 on 2019-11-21 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191121_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='concessionaria',
            name='cnpj',
            field=models.CharField(default=1234, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('AB', 'ABERTO'), ('PD', 'PRODUCAO'), ('AG', 'AGUARDANDO RETIRADA')], default='AB', max_length=15),
        ),
    ]
