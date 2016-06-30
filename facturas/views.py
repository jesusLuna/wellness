# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from facturas.forms import FacturaForm
from facturas.models import Factura


# Create your views here.
def index(request):
    return render_to_response('index.html',
                              {},
                              context_instance=RequestContext(request))


def my_view(request, codigo=None):
    form = FacturaForm()
    return render_to_response('item.html',
                              {'form': form},
                              context_instance=RequestContext(request))
