from django.conf.urls import url, include
from django.contrib import admin

from autenticacao.views import Autenticacao, Index, NovoPedido, Contato, Logout



urlpatterns = [
    url(r'^$', Autenticacao.as_view(), name='autenticacao'),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^novo_pedido/', NovoPedido.as_view(), name='novo_pedido'),
    url(r'^contato/', Contato.as_view(), name='contato'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
]
