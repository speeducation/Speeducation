# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lineas', '0001_initial'),
        ('alumnos', '0011_auto_20151120_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comportamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
                ('conducta', models.ForeignKey(to='lineas.Conducta')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('evaluacionInicial', models.CharField(choices=[('Ineficiente', 1), ('Bueno', 2), ('Excelente', 3)], max_length=20, default=0)),
                ('evaluacionMedia', models.CharField(choices=[('Ineficiente', 1), ('Bueno', 2), ('Excelente', 3)], max_length=20, default=0)),
                ('evaluacionFinal', models.CharField(choices=[('Ineficiente', 1), ('Bueno', 2), ('Excelente', 3)], max_length=20, default=0)),
                ('actividad', models.ForeignKey(to='lineas.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('fechaInicio', models.DateField(default=datetime.datetime(2015, 12, 7, 10, 51, 46, 156542, tzinfo=utc))),
                ('fechaFinal', models.DateField(default=datetime.datetime(2015, 12, 7, 10, 51, 46, 156574, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='PlanEstudio',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
                ('linea', models.ForeignKey(to='lineas.Linea')),
                ('periodo', models.ForeignKey(default='', to='alumnos.Periodo')),
            ],
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='plan',
            field=models.ForeignKey(default='', to='alumnos.PlanEstudio'),
        ),
    ]
