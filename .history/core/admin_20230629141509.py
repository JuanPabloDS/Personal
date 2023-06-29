from django.contrib import admin
from django import forms
from django.conf import settings
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


class ColorPickerWidget(forms.TextInput):
    class Media:
        js = (f'{settings.STATIC_URL}admin/js/django-admin-colorpicker.js',)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)
        color = value if value else '#000000'
        widget_attrs = attrs.copy()
        widget_attrs['type'] = 'text'
        widget_attrs['style'] = 'width: 70px;'
        return mark_safe(
            f'{rendered}'
            f'<input type="color" value="{color}" class="color-picker" style="margin-left: 5px;">'
            f'<script>'
            f'window.addEventListener("DOMContentLoaded", function() {{'
            f'    var inputElem = document.querySelector("input.color-picker");'
            f'    var textElem = document.querySelector("input[name=\'{name}\']");'
            f'    inputElem.addEventListener("change", function() {{'
            f'        textElem.value = inputElem.value;'
            f'    }});'
            f'}});'
            f'</script>'
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



