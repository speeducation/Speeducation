# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0004_auto_20151108_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='sexo',
            field=models.CharField(max_length=50, default=(('H', 'Hombre'), ('M', 'Mujer')), choices=[('H', 'Hombre'), ('M', 'Mujer')]),
        ),
    ]
