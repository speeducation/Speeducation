# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('apellido', models.CharField(max_length=50, null=True, blank=True)),
                ('fechaNacimiento', models.DateField()),
                ('bio', models.TextField(max_length=500)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
