# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('codigo', models.CharField(max_length=9, serialize=False, verbose_name=b'C\xc3\xb3digo', primary_key=True)),
                ('cliente', models.CharField(max_length=50, verbose_name=b'Cliente')),
                ('fecha', models.DateField(verbose_name=b'Fecha')),
                ('inicio_periodo', models.DateField(verbose_name=b'Inicio periodo')),
                ('fin_periodo', models.DateField(verbose_name=b'Fin periodo')),
                ('total', models.FloatField(verbose_name=b'Total')),
            ],
        ),
    ]
