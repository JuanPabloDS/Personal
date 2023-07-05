from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import (Apresentacao, Sobre, SobreDados, Detalhes,Precos, PrecosPlano1, PrecosPlano1Dados,
PrecosPlano2Dados, PrecosPlano2, Imagem, ImagensLista, Duvidas, DuvidasRespostas, Contato, Cores, Icone)

class IndexView(TemplateView):

    def get(self, request):

            def vericarVazio(classe):
                if not len(classe) == 0:
                    return classe[0]
                else:
                    return

            personal = Apresentacao.objects.all()
            personal_item = vericarVazio(personal)

            sobre = Sobre.objects.all()
            sobre_item = vericarVazio(sobre)
            sobre_dados = SobreDados.objects.all()

            detalhes = Detalhes.objects.all()

            preco_all = Precos.objects.all()
            precos = vericarVazio(preco_all)

            precos_plano1_all = PrecosPlano1.objects.all()
            precos_plano1 = vericarVazio(precos_plano1_all)
            precos_plano1_dados = PrecosPlano1Dados.objects.all()
            
            precos_plano2_all = PrecosPlano2.objects.all()
            precos_plano2 = vericarVazio(precos_plano2_all)
            precos_plano2_dados = PrecosPlano2Dados.objects.all()

            imagem_all = Imagem.objects.all()
            imagem = vericarVazio(imagem_all)
            imagem_lista = ImagensLista.objects.all()

            duvidas_all = Duvidas.objects.all()
            duvidas = vericarVazio(duvidas_all)
            duvidas_respostas = DuvidasRespostas.objects.all()

            contato_all = Contato.objects.all()
            contato = vericarVazio(contato_all)

            cores_all = Cores.objects.all()
            cores = vericarVazio(cores_all)

            icone_all = Icone.objects.all()
            icone = vericarVazio(icone_all)

            context = {
                'projetos': personal_item,
                'sobre': sobre_item,
                'sobre_dados': sobre_dados,
                'detalhes': detalhes,
                'precos': precos,
                'precos_plano1': precos_plano1,
                'precos_plano1_dados': precos_plano1_dados,
                'precos_plano2': precos_plano2,
                'precos_plano2_dados': precos_plano2_dados,
                'imagem': imagem,
                'imagem_lista': imagem_lista,
                'duvidas': duvidas,
                'duvidas_respostas': duvidas_respostas,
                'contato': contato,
                'cores' : cores,
                'icone' : icone,

            }

            return render( request, 'index.html', context)

    template_name: str = 'index.html'

