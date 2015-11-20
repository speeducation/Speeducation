# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0009_auto_20151120_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2015, 11, 20, 2, 44, 5, 838794, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='grupo',
            field=models.CharField(max_length=5),
        ),
    ]
