from principal.models import Avaliacao, Restaurante
from principal.forms import AvaliacaoForm
from django.db.models import Avg
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class AvaliacaoCreateView(SuccessMessageMixin, CreateView):
    template_name = 'restaurante.html'
    form_class = AvaliacaoForm
    model = Avaliacao
    success_message = 'Avaliação publicada com sucesso'

    def get_success_url(self, *args, **kwargs):
        url_redir = reverse('visualizar_restaurante', kwargs={'pk': self.kwargs['pk']})
        if self.request.user.perfil.grupo == 'E':
            url_redir += '#message-box-success'
        return url_redir

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['autor'] = self.request.user.id
        initial['restaurante'] = self.kwargs['pk']
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurante'] = Restaurante.objects.annotate(nota=Avg('avaliacoes__nota')).get(pk=self.kwargs['pk'])
        context['avaliacaoUsuario'] = context['restaurante'].avaliacoes.filter(autor__id=self.request.user.id).first()
        avaliacoes = context['restaurante'].avaliacoes.exclude(autor__id=self.request.user.id)
        context['avaliacoes'] = avaliacoes if avaliacoes.count() > 0 else None
        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.restaurante = Restaurante.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class AvaliacaoDeleteView(DeleteView):
    model = Avaliacao
    success_message = 'Avaliação excluída com sucesso'

    def get_success_url(self, *args, **kwargs):
        url_redir = reverse('visualizar_restaurante', kwargs={'pk': self.kwargs['restaurante_pk']})
        if self.request.user.perfil.grupo == 'E':
            url_redir += '#message-box-success'
        return url_redir
    
    # Redireciona quaisquer requisições GET para requisições POST, para que
    # a exclusão ocorra diretamente, sem formulário de confirmação de exclusão
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # Código necessário apenas para exibir a mensagem de sucesso
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AvaliacaoDeleteView, self).delete(request, *args, **kwargs)

class AvaliacaoUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'restaurante.html'
    form_class = AvaliacaoForm
    model = Avaliacao
    success_message = 'Avaliação alterada com sucesso'

    def get_success_url(self, *args, **kwargs):
        url_redir = reverse('visualizar_restaurante', kwargs={'pk': self.kwargs['restaurante_pk']})
        if self.request.user.perfil.grupo == 'E':
            url_redir += '#message-box-success'
        return url_redir

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurante'] = Restaurante.objects.annotate(nota=Avg('avaliacoes__nota')).get(pk=self.kwargs['restaurante_pk'])
        context['avaliacaoUsuario'] = context['restaurante'].avaliacoes.filter(autor__id=self.request.user.id).first()
        avaliacoes = context['restaurante'].avaliacoes.exclude(autor__id=self.request.user.id)
        context['avaliacoes'] = avaliacoes if avaliacoes.count() > 0 else None
        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.restaurante = Restaurante.objects.get(pk=self.kwargs['restaurante_pk'])
        return super().form_valid(form)