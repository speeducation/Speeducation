# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maestros', '0006_auto_20151120_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maestro',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='email',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='username',
        ),
        migrations.AddField(
            model_name='maestro',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=-2003),
            preserve_default=False,
        ),
    ]
