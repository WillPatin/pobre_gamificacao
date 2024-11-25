# Generated by Django 5.1.3 on 2024-11-25 00:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao_app', '0003_remove_selo_usuarios'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='selo',
            name='usuarios',
            field=models.ManyToManyField(blank=True, related_name='selos', to=settings.AUTH_USER_MODEL),
        ),
    ]
