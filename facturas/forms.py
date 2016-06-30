from djng.forms import NgModelFormMixin, NgModelForm

from facturas.models import Factura


class FacturaForm(NgModelFormMixin, NgModelForm):
    class Meta:
        model = Factura
        exclude = ()
