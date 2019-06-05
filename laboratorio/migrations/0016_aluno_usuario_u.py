# Generated by Django 2.2.1 on 2019-05-29 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laboratorio', '0015_remove_aluno_usuario_u'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='usuario_u',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
