# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0010_auto_20151120_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fecha_registro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
