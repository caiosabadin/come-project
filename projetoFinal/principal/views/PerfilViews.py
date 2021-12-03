from django.views.generic import DetailView, UpdateView
from principal.models import Perfil, Avaliacao
from principal.forms import PerfilForm
from django.contrib.messages.views import SuccessMessageMixin

class PerfilDetailView(DetailView):
    
    model = Perfil
    context_object_name = 'perfil'
    template_name = 'perfil.html'

    def get_object(self, queryset=None):
        return Perfil.objects.get(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avaliacoes'] = Avaliacao.objects.filter(autor__id=self.request.user.id)
        return context

class PerfilUpdateView(SuccessMessageMixin, UpdateView):

    model = Perfil
    context_object_name = 'perfil'
    template_name = 'editar_perfil.html'
    form_class = PerfilForm
    success_url = '/perfil'
    success_message = 'Seu perfil foi atualizado com sucesso.'

    def get_object(self, queryset=None):
        return Perfil.objects.get(id=self.request.user.id)
