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
        css = {
            'all': ('admin/css/widgets.css',)
        }
        js = ('admin/js/jquery.init.js', 'admin/js/jquery.colorpicker.js', 'admin/js/django-admin-colorpicker.js')

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)
        color = value if value else '#000000'
        widget_attrs = attrs.copy()
        widget_attrs['type'] = 'text'
        widget_attrs['style'] = 'width: 70px;'
        input_id = widget_attrs.pop('id', '')  # Obtém o ID do campo
        return mark_safe(
            f'{rendered}'
            f'<div style="display: flex; align-items: center;" id="color-picker-{input_id}">'
            f'    <input type="color" value="{color}" class="color-picker" id="color--{input_id}" style="margin-left: 5px;">'
            f'    <input type="text" value="{color}" class="color-hex" id="color-hex-{input_id}" style="width: 80px; margin-left: 5px; display:none">'
            f'</div>'
            f'<script>'
            f'window.addEventListener("DOMContentLoaded", function() {{'
            f'    var colorElem = document.querySelector("#color--{input_id}");'
            f'    var textElem = document.querySelector("#color-hex-{input_id}");'
            f'    var inputElem = document.querySelector("#{input_id}");'
            f'    colorElem.addEventListener("change", function() {{'
            f'        inputElem.value = colorElem.value;'
            f'    }});'
            f'    inputElem.addEventListener("change", function() {{'
            f'        colorElem.value = inputElem.value;'
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
            'cor_titulo': ColorPickerWidget(),
            'cor_titulo_dois': ColorPickerWidget(),
            'cor_fundo_pagina': ColorPickerWidget(),
            'cor_menu': ColorPickerWidget(),
            'cor_paragrafo': ColorPickerWidget(),
            'cor_sublinhado_titulo': ColorPickerWidget(),
            'cor_box': ColorPickerWidget(),
            'cor_sobre': ColorPickerWidget(),
            'cor_back_text': ColorPickerWidget(),
            'cor_sobre_fundo': ColorPickerWidget(),
            'cor_sobre_titulo': ColorPickerWidget(),
            'cor_price_fundo': ColorPickerWidget(),
            'cor_price_titulo': ColorPickerWidget(),
            'cor_price_texto': ColorPickerWidget(),
            'cor_price_money': ColorPickerWidget(),
            'cor_price_box': ColorPickerWidget(),
            'cor_price_value': ColorPickerWidget(),
            'cor_price_span': ColorPickerWidget(),
            'cor_price_pg': ColorPickerWidget(),
            'cor_imagem_fundo': ColorPickerWidget(),
            'cor_imagem_titulo': ColorPickerWidget(),
            'cor_question_fundo': ColorPickerWidget(),
            'cor_question_titulo': ColorPickerWidget(),
            'cor_question_texto': ColorPickerWidget(),
            'cor_question_box': ColorPickerWidget(),
            'cor_question_span': ColorPickerWidget(),
            'cor_contact_fundo': ColorPickerWidget(),
            'cor_contact_titulo': ColorPickerWidget(),
            'cor_contact_texto': ColorPickerWidget(),
            'cor_contact_box': ColorPickerWidget(),
            'cor_contact_span': ColorPickerWidget(),
            'cor_titulo': ColorPickerWidget(),
        }

class CoresAdmin(admin.ModelAdmin):
    form = CoresForm

admin.site.register(Cores, CoresAdmin)

class DetalhesCoresForm(forms.ModelForm):
    class Meta:
        model = Detalhes
        fields = '__all__'
        widgets = {
            'cor_titulo': ColorPickerWidget(),
            'cor_fundo': ColorPickerWidget(),
            'cor_texto': ColorPickerWidget(),
        }

class DetalhesCoresAdmin(admin.ModelAdmin):
    form = DetalhesCoresForm


admin.site.register(Detalhes,DetalhesCoresAdmin)

