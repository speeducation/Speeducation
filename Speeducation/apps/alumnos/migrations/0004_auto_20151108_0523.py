# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_alumnos_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_registro', models.DateField(default=datetime.datetime(2015, 11, 8, 5, 23, 44, 521521, tzinfo=utc))),
                ('grupo', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('maestro', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='comportamientos',
            name='alumnos',
        ),
        migrations.RemoveField(
            model_name='evaluaciones',
            name='planActividad',
        ),
        migrations.RemoveField(
            model_name='planactividades',
            name='alumno',
        ),
        migrations.DeleteModel(
            name='Alumnos',
        ),
        migrations.DeleteModel(
            name='Comportamientos',
        ),
        migrations.DeleteModel(
            name='Evaluaciones',
        ),
        migrations.DeleteModel(
            name='PlanActividades',
        ),
    ]
