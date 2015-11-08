# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_auto_20151108_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2015, 11, 8, 5, 27, 37, 122235, tzinfo=utc)),
        ),
    ]
