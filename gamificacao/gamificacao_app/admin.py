from django.contrib import admin
from .models import Selo, Transacao

@admin.register(Selo)
class SeloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')
    
@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'valor', 'data')
