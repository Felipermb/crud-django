from django.conf.urls import url, include
from django.contrib import admin

from autenticacao.views import Autenticacao, Index



urlpatterns = [
    url(r'^$', Autenticacao.as_view(), name='autenticacao'),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]