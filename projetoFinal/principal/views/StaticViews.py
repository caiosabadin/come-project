from django.views.generic import TemplateView
from principal.models import Imagem

class AcessibilidadeView(TemplateView):
    template_name = "acessibilidade.html"

    def get_context_data(self, **kwargs):
        context = super(AcessibilidadeView, self).get_context_data(**kwargs)
        context['imagem'] = Imagem.objects.get(pk=22)
        return context

class CozinhasView(TemplateView):
    template_name = "cozinhas.html"

class EventosView(TemplateView):
    template_name = "eventos.html"

class FinancasView(TemplateView):
    template_name = "financas.html"

    def get_context_data(self, **kwargs):
        context = super(FinancasView, self).get_context_data(**kwargs)
        context['graficos'] = Imagem.objects.filter(pk__in=[18, 19, 20])
        return context

class IncluirEstabelecimentoView(TemplateView):
    template_name = "incluir_estabelecimento.html"

    def get_context_data(self, **kwargs):
        context = super(IncluirEstabelecimentoView, self).get_context_data(**kwargs)
        context['imagem'] = Imagem.objects.get(pk=23)
        return context

class MapaDoSiteView(TemplateView):
    template_name = "mapa_site.html"

class MissaoView(TemplateView):
    template_name = "missao.html"

    def get_context_data(self, **kwargs):
        context = super(MissaoView, self).get_context_data(**kwargs)
        context['imagem'] = Imagem.objects.get(pk=24)
        return context

class PerguntasFrequentesView(TemplateView):
    template_name = "perguntas_frequentes.html"

    def get_context_data(self, **kwargs):
        context = super(PerguntasFrequentesView, self).get_context_data(**kwargs)
        context['imagem'] = Imagem.objects.get(pk=21)
        return context

class TrabalheConoscoView(TemplateView):
    template_name = "trabalhe_conosco.html"