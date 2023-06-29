from django.contrib import admin
from django import forms
from colorful.fields import RGBColorField
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from .models import (Apresentacao, Sobre, SobreDados, Detalhes,Precos, PrecosPlano1, PrecosPlano1Dados,
PrecosPlano2Dados, PrecosPlano2, Imagem, ImagensLista, Duvidas, DuvidasRespostas, Contato, Cores)


class LimitAdmin(admin.ModelAdmin):
    limit = 1  # Defina o limite máximo de cadastros

    def has_add_permission(self, request):
        # Verifica se o número de instâncias existentes atingiu o limite máximo
        if self.model.objects.count() >= self.limit:
            return False  # Impede a criação de novas instâncias
        return super().has_add_permission(request)

admin.site.register(Apresentacao, LimitAdmin)
admin.site.register(Sobre, LimitAdmin)
admin.site.register(SobreDados)
admin.site.register(Detalhes)
admin.site.register(Precos, LimitAdmin)
admin.site.register(PrecosPlano1)
admin.site.register(PrecosPlano1Dados)
admin.site.register(PrecosPlano2)
admin.site.register(PrecosPlano2Dados)
admin.site.register(Imagem)
admin.site.register(ImagensLista)
admin.site.register(Duvidas)
admin.site.register(DuvidasRespostas)
admin.site.register(Contato)


class ColorPickerWidget(TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)
        color = value if value else '#000000'
        return mark_safe(
            f'{rendered}'
            f'<input type="color" value="{color}" style="height: 30px; width: 30px; padding: 0; margin-left: 5px;">'
        )

class CoresForm(forms.ModelForm):
    class Meta:
        model = Cores
        fields = '__all__'
        widgets = {
            'cor_titulo': ColorPickerWidget(),
        }

class CoresAdmin(admin.ModelAdmin):
    form = CoresForm

admin.site.register(Cores, CoresAdmin)



