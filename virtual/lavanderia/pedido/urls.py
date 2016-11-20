
from django.conf.urls import url
from pedido.views import *

urlpatterns = [
    url(r'^novo_pedido/', NovoPedido.as_view(), name='novo-pedido'),
]