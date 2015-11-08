# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20151108_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
