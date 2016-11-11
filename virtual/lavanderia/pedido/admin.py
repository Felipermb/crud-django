from django.contrib import admin
from .models import Pedido, TipoRoupa


class TipoRoupaInline(admin.StackedInline):
    model = TipoRoupa
    extra = 1
    max_num = 5

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    inlines = [ TipoRoupaInline, ]
    exclude = ["valor_pedido"]




admin.site.register(Pedido, PedidoAdmin)
admin.site.register(TipoRoupa)
