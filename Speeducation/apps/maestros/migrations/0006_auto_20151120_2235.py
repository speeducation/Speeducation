# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0005_auto_20151109_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='nombre',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
