# Generated by Django 5.1.3 on 2024-11-25 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao_app', '0002_selo_usuarios_transacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selo',
            name='usuarios',
        ),
    ]
