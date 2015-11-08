# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comportamientos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluacionInicial', models.IntegerField(choices=[(b'Ineficiente', 1), (b'Bueno', 2), (b'Excelente', 3)])),
                ('evaluacionMedia', models.IntegerField(choices=[(b'Ineficiente', 1), (b'Bueno', 2), (b'Excelente', 3)])),
                ('evaluacionFinal', models.IntegerField(choices=[(b'Ineficiente', 1), (b'Bueno', 2), (b'Excelente', 3)])),
            ],
        ),
        migrations.CreateModel(
            name='PlanActividades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finalizado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='alumnos',
            name='sexo',
            field=models.CharField(default=((b'H', b'Hombre'), (b'M', b'Mujer')), max_length=50, choices=[(b'H', b'Hombre'), (b'M', b'Mujer')]),
        ),
        migrations.AddField(
            model_name='planactividades',
            name='alumno',
            field=models.ForeignKey(to='alumnos.Alumnos'),
        ),
        migrations.AddField(
            model_name='evaluaciones',
            name='planActividad',
            field=models.OneToOneField(to='alumnos.PlanActividades'),
        ),
        migrations.AddField(
            model_name='comportamientos',
            name='alumnos',
            field=models.ForeignKey(to='alumnos.Alumnos'),
        ),
    ]
