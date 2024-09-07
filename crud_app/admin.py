from django.contrib import admin
from .models import Artigo

class ArtigoAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista de artigos
    list_display = ('titulo', 'autores', 'data_ano')

    # Campos a serem exibidos no formulário de criação/edição
    fields = ('titulo', 'autores', 'resumo', 'abstract', 'palavras_chave', 'data_ano', 'revista', 'arquivo')

admin.site.register(Artigo, ArtigoAdmin)