from django.contrib import admin
from .models import Cliente, Produto
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome', 'sobrenome', 'email')
    search_fields=('nome', 'sobrenome', 'email')
    list_filter=('nome', 'sobrenome', 'email')

class ProdutoAdmin(admin.ModelAdmin):
    list_display=('nome', 'preço', 'estoque')
    search_fields = ('nome', 'preço')
    list_filter = ('nome', 'preço')

admin.site.register(Cliente)
admin.site.register(Produto)