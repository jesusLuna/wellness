# -*- coding: utf-8 -*-
from django.db import models

from djng.views.crud import NgCRUDView


# Create your models here.
class Factura(models.Model):
    codigo = models.CharField('Código', max_length=9, primary_key=True)
    cliente = models.CharField('Cliente', max_length=50)
    fecha = models.DateField('Fecha')
    inicio_periodo = models.DateField('Inicio periodo')
    fin_periodo = models.DateField('Fin periodo')
    total = models.FloatField('Total')


class MyCRUDView(NgCRUDView):
    model = Factura
