# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0008_auto_20151109_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2015, 11, 20, 2, 38, 40, 243371, tzinfo=utc)),
        ),
    ]
