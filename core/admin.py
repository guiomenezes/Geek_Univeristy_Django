from django.contrib import admin
from .models import Clientes, Produtos


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email')


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Produtos, ProdutosAdmin)
