from django.contrib import admin
from django import forms
from .models import (Apresentacao, Sobre, SobreDados, Detalhes,Precos, PrecosPlano1, PrecosPlano1Dados,
PrecosPlano2Dados, PrecosPlano2, Imagem, ImagensLista, Duvidas, DuvidasRespostas, Contato, Cores)


class ApresentacaoAdmin(admin.ModelAdmin):
    max_num = 1

admin.site.register(Apresentacao, ApresentacaoAdmin)