# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0002_auto_20151108_0402'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Maestro',
        ),
    ]
