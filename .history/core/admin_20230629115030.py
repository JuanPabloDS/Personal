from django.contrib import admin
from django import forms
from .models import (Apresentacao, Sobre, SobreDados, Detalhes,Precos, PrecosPlano1, PrecosPlano1Dados,
PrecosPlano2Dados, PrecosPlano2, Imagem, ImagensLista, Duvidas, DuvidasRespostas, Contato, Cores)


class ApresentacaoAdmin(admin.ModelAdmin):
    limit = 1  # Defina o limite máximo de cadastros

    def has_add_permission(self, request):
        # Verifica se o número de instâncias existentes atingiu o limite máximo
        if self.model.objects.count() >= self.limit:
            return False  # Impede a criação de novas instâncias
        return super().has_add_permission(request)

admin.site.register(Apresentacao, ApresentacaoAdmin, Sobre)