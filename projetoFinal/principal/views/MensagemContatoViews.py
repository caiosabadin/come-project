from principal.models import MensagemContato, Imagem
from principal.forms import MensagemContatoForm
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

class MensagemContatoCreateView(SuccessMessageMixin, CreateView):
    template_name = 'contato.html'
    form_class = MensagemContatoForm
    model = MensagemContato
    success_message = 'Sua mensagem foi enviada. A equipe agradece seu contato'

    def get_success_url(self, *args, **kwargs):
        if self.kwargs.get("tipo", 'outro') != 'outro':
            return reverse('enviar_mensagem', kwargs={'tipo': self.kwargs['tipo']})
        else:
            return reverse('enviar_mensagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_contato = self.kwargs.get("tipo", 'outro')
        indices = {'sugestao': 'sugestão', 'duvida': 'dúvida', 'reclamacao': 'reclamação', 'outro': 'contato'}
        context['tipo_contato'] = indices[tipo_contato]
        context['imagem'] = Imagem.objects.get(titulo='Contato')
        return context

    def form_valid(self, form):
        tipo_contato = self.kwargs.get("tipo", 'outro')
        indices = {'sugestao': 1, 'duvida': 2, 'reclamacao': 3, 'outro': 4}
        form.instance.tipo_contato = indices[tipo_contato]
        form.instance.usuario = self.request.user
        return super().form_valid(form)