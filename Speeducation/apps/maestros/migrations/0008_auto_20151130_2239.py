# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0007_auto_20151130_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maestro',
            name='id',
        ),
        migrations.AlterField(
            model_name='maestro',
            name='sexo',
            field=models.CharField(default=(('H', 'Hombre'), ('M', 'Mujer')), choices=[('H', 'Hombre'), ('M', 'Mujer')], null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='maestro',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='maestro',
            name='user',
            field=models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True, related_name='user'),
        ),
    ]
