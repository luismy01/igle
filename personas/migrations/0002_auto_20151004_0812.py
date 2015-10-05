# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='genero',
            field=models.CharField(default=b'M', max_length=3, choices=[(b'F', b'Mujer'), (b'M', b'Hombre')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='identificacion_tipo',
            field=models.CharField(default=b'CC', max_length=3, choices=[(b'CC', b'Cedula de ciudadania'), (b'TI', b'Tarjeta de identidad'), (b'PS', b'Pasaporte')]),
        ),
    ]
