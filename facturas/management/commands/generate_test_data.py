# -*- coding: utf-8 -*-

import datetime

from optparse import make_option

from django.core.management.base import BaseCommand

from facturas.models import Factura
from facturas.utils import ask_for_confirmation


class Command(BaseCommand):
    help = 'Generate some test data'

    option_list = BaseCommand.option_list + (
        make_option('--verbose', action='store_true', dest='verbose',
                    default=False, help='Verbose mode'),
    )

    def handle(self, *args, **options):
        if not ask_for_confirmation('Do you want to generate test data?'):
            return
        Factura.objects.create(codigo='sfljhb83b', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=1, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=1, day=1),
            fin_periodo=datetime.datetime(year=2015, month=1, day=31),
            total=48.26)
        Factura.objects.create(codigo='hgvlk99jk', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=2, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=2, day=1),
            fin_periodo=datetime.datetime(year=2015, month=2, day=28),
            total=39.59)
        Factura.objects.create(codigo='ljhbsd31d', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=3, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=3, day=1),
            fin_periodo=datetime.datetime(year=2015, month=3, day=31),
            total=34.80)
        Factura.objects.create(codigo='nvksid83g', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=4, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=4, day=1),
            fin_periodo=datetime.datetime(year=2015, month=4, day=30),
            total=102.53)
        Factura.objects.create(codigo='kjsoiv32k', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=5, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=5, day=1),
            fin_periodo=datetime.datetime(year=2015, month=5, day=31),
            total=34.23)
        Factura.objects.create(codigo='makpos12l', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=6, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=6, day=1),
            fin_periodo=datetime.datetime(year=2015, month=6, day=30),
            total=23.49)
        Factura.objects.create(codigo='siomkq32m', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=7, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=7, day=1),
            fin_periodo=datetime.datetime(year=2015, month=7, day=31),
            total=123.59)
        Factura.objects.create(codigo='slkjns00y', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=8, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=8, day=1),
            fin_periodo=datetime.datetime(year=2015, month=8, day=31),
            total=90.89)
        Factura.objects.create(codigo='mwkiqq69c', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=9, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=9, day=1),
            fin_periodo=datetime.datetime(year=2015, month=9, day=30),
            total=56.29)
        Factura.objects.create(codigo='lmksww19d', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=10, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=10, day=1),
            fin_periodo=datetime.datetime(year=2015, month=10, day=31),
            total=89.77)
        Factura.objects.create(codigo='jovssm93c', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=11, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=11, day=1),
            fin_periodo=datetime.datetime(year=2015, month=11, day=30),
            total=44.76)
        Factura.objects.create(codigo='nsvsls02c', cliente='Jesús Luna',
            fecha=datetime.datetime(year=2015, month=12, day=5),
            inicio_periodo=datetime.datetime(year=2015, month=12, day=1),
            fin_periodo=datetime.datetime(year=2015, month=12, day=31),
            total=76.32)
