from django.conf.urls import url, include
from django.contrib import admin

# from autenticacao.views import Autenticacao, Index, Contato, Logout
# from pedido.views import NovoPedido



urlpatterns = [
    url(r'^', include('autenticacao.urls')),
    url(r'^pedido/', include('pedido.urls')),
    url(r'^admin/', admin.site.urls),
]


