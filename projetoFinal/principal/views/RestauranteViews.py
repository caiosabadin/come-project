from principal.models import Restaurante
from principal.forms import AvaliacaoForm
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.db.models import Avg, Q
from math import ceil

def converteRestaurantesToJson(restaurantes):
    objetos = {'restaurantes': []}
    for restaurante in restaurantes:
        if restaurante.nota is not None:
            restaurante.nota = int(ceil(restaurante.nota))
        pratos = []
        for prato in restaurante.pratos.all():
            pratos.append({'id': prato.id, 'nome': prato.nome})
        fotos = []
        for foto in restaurante.fotos.all():
            fotos.append({'id': foto.id, 'endereco': str(foto.endereco), 'descricao': foto.descricao})
        objetos['restaurantes'].append({'id': restaurante.id, 'fotos': fotos, 'nome': restaurante.nome, 'endereco': str(restaurante.endereco), 'sobre': restaurante.sobre, 'pratos': pratos, 'nota': restaurante.nota})            
    return objetos

class RestauranteListView(ListView):

    template_name = 'index.html'
    context_object_name = 'restaurantes'
    model = Restaurante

    def get(self, request, *args, **kwargs):

        # Se não foi solicitado um arquivo JSON à view por meio do parâmetro
        # get 'j', retorne o método get normal, da classe acima (ListView)
        # Senão, retorne um arquivo JSON com os dados solicitados.

        if 'j' not in self.request.GET:
            return super().get(self, request, *args, **kwargs)
        else:
            restaurantes = self.get_queryset()
            restaurantes_json = converteRestaurantesToJson(restaurantes)
            return JsonResponse(restaurantes_json, status=200)


    def get_queryset(self, *args, **kwargs):

        # Se o parâmetro get 'p' foi passado, então o que está sendo buscado é
        # apenas uma lista de restaurantes que contêm o pratos cujo id é o
        # valor do parâmetro. Portanto, demais parâmetros são ignorados.
        # Senão, ele analisará os demais parâmetros: 'b', que guarda os termos
        # buscados, e os parâmetros das checkboxes das cidades: 'rj', 'cb',
        # 'sp' e 'bh'. Então, retornará uma lista de restaurantes conforme os
        # parâmetros passados.

        if 'p' in self.request.GET:
            # Se for passado ao parâmetro algum valor id que não seja válido,
            # serão retornados os restaurantes sem usar filtro algum.
            try:
                id_prato = int(self.request.GET['p'])
                return Restaurante.objects.annotate(nota=Avg('avaliacoes__nota')).filter(Q(pratos__id=id_prato)).distinct()
            except:
                return Restaurante.objects.annotate(nota=Avg('avaliacoes__nota'))
        else:
            # Popula os filtros por cidade. A query retornará os restaurantes
            # que existem em uma cidade ou os que existem na outra. Ou seja, é
            # um filtro inclusivo, e não exclusivo.

            filtros_localizacao = None
            if 'rj' in self.request.GET:
                filtros_localizacao = Q(endereco__estado='RJ')
            if 'sp' in self.request.GET:
                if filtros_localizacao is None:
                    filtros_localizacao = Q(endereco__estado='SP')
                else:
                    filtros_localizacao |= Q(endereco__estado='SP')
            if 'bh' in self.request.GET:
                if filtros_localizacao is None:
                    filtros_localizacao = Q(endereco__estado='MG')
                else:
                    filtros_localizacao |= Q(endereco__estado='MG')
            if 'cb' in self.request.GET:
                if filtros_localizacao is None:
                    filtros_localizacao = Q(endereco__estado='PR')
                else:
                    filtros_localizacao |= Q(endereco__estado='PR')

            # Popula o filtro que busca os termos. O valor do parâmetro é
            # separado em várias strings (termos), e só se o nome de um
            # restaurante contiver o termo buscado ou só se o nome de um dos
            # pratos do restaurante contiver o termo buscado, o restaurante
            # entrará para a listagem.

            filtros_termo = None
            if 'b' in self.request.GET:
                termos = self.request.GET['b'].split()
                for termo in termos:
                    if filtros_termo is None:
                        filtros_termo = Q(nome__icontains=termo) | Q(pratos__nome__icontains=termo)
                    else:
                        filtros_termo |= Q(nome__icontains=termo) | Q(pratos__nome__icontains=termo)
            
            # Prepara a junção dos filtros finais à query. Se houver apenas o
            # filtro por termos, os filtros finais aplicados serão somente os
            # por termos. Se houver apenas o filtro por localização, o filtro
            # final aplicado será somente o por localização. Se ambos filtros
            # por localização e por termo existirem, então serão inclusos na
            # listagem só os restaurantes que satisfaçam ambos os filtros (E)

            filtros = None
            if filtros_localizacao is None and filtros_termo is not None:
                filtros = filtros_termo
            elif filtros_localizacao is not None and filtros_termo is None:
                filtros = filtros_localizacao
            elif filtros_localizacao is not None and filtros_termo is not None:
                filtros = filtros_termo & filtros_localizacao

            # Se não houver filtro algum, retorna todos os restaurantes; do
            # contrário, retorna os restaurantes encontrados com base nos
            # filtros definidos nas linhas acima.
            return Restaurante.objects.annotate(nota=Avg('avaliacoes__nota')) if filtros is None else Restaurante.objects.annotate(nota=Avg('avaliacoes__nota')).filter(filtros).distinct()

    def get_paginate_by(self, queryset):
        # Se for solicitado um arquivo JSON, o que é feito com o parâmetro
        # 'j', não permite paginação; senão, será paginado 5 a 5 itens.
        return None if 'j' in self.request.GET else 5

class RestauranteDetailView(DetailView):

    model = Restaurante
    context_object_name = 'restaurante'
    template_name = 'restaurante.html'

    def get_object(self, queryset=None):
        restaurante = Restaurante.objects.annotate(nota=Avg('avaliacoes__nota')).get(pk=self.kwargs['pk'])
        return restaurante

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AvaliacaoForm(autor=self.request.user.id, initial={'autor': self.request.user.id, 'restaurante': self.kwargs['pk']})
        context['avaliacaoUsuario'] = self.object.avaliacoes.filter(autor__id=self.request.user.id).first()
        avaliacoes = self.object.avaliacoes.exclude(autor__id=self.request.user.id)
        context['avaliacoes'] = avaliacoes if avaliacoes.count() > 0 else None
        print(context['avaliacoes'])
        return context