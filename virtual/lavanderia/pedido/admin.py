# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Pedido


# class TipoRoupaInline(admin.StackedInline):
#     model = TipoRoupa
#     extra = 0
#     max_num = 10

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    # inlines = [ TipoRoupaInline, ]
    exclude = ["valor_pedido"]




admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(TipoRoupa)
