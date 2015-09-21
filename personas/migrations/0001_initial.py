# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('identificacion_tipo', models.CharField(default=b'CC', max_length=3, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')])),
                ('identificacion_codigo', models.CharField(max_length=30, db_index=True)),
                ('congregacion', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=50)),
                ('genero', models.CharField(default=b'M', max_length=3, choices=[(b'F', b'Femenino'), (b'M', b'Masculino')])),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
    ]
