# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0003_auto_20151108_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maestro',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='password',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='user_permissions',
        ),
    ]
