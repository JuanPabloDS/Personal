# Generated by Django 3.2 on 2023-06-30 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230629_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apresentacao',
            old_name='iamgem_fundo',
            new_name='imagem_back',
        ),
    ]
