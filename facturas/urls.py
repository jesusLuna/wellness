from django.conf.urls import patterns, url

from facturas.models import MyCRUDView

urlpatterns = patterns(
    'facturas.views',
    url(r'^index/?$', 'index', name='index'),
    url(r'^crud/list/?$', MyCRUDView.as_view(), name='my_crud_view'),
    url(r'^crud/item/(?P<codigo>.+)/$', 'my_view', name='my_view'),
    url(r'^crud/item/?$', 'my_view', name='my_view'),
)
