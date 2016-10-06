from django.conf.urls import url, include
from django.contrib import admin

from autenticacao.views import Autenticacao

urlpatterns = [
    url(r'^$', Autenticacao.as_view(), name='autenticacao'),
    url(r'^admin/', admin.site.urls),
]