# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=75, unique=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conducta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=75, unique=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('updated', models.DateTimeField(null=True, auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='conducta',
            name='linea',
            field=models.ForeignKey(to='lineas.Linea'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='linea',
            field=models.ForeignKey(to='lineas.Linea'),
        ),
    ]
