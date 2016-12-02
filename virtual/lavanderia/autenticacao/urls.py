
from django.conf.urls import url
from autenticacao.views import *

urlpatterns = [
    url(r'^$', Autenticacao.as_view(), name='autenticacao'),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^contato/', Contato.as_view(), name='contato'),
    url(r'^help/', Help.as_view(), name='help'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^cartao/', NovoCartao.as_view(), name='cartao'),
    url(r'^endereco/', NovoEndereco.as_view(), name='endereco'),
    url(r'^listar-cartao/', ListarCartao.as_view(), name='listar_cartao'),
    url(r'^listar-endereco/', ListarEndereco.as_view(), name='listar_endereco'),
    url(r'^(?P<pk>[0-9]+)/$', DeletarCartao.as_view(), name='deletar_cartao'),
    url(r'^(?P<pk>[0-9]+)/(?P<cep>[0-9]{8})/$', DeletarEndereco.as_view(), name='deletar_endereco'),

]
