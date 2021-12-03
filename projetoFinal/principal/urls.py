from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from principal import views
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

urlpatterns = [
    path('', login_required(views.RestauranteListView.as_view()), name='index'),
    path('restaurante/<int:pk>', login_required(views.AvaliacaoCreateView.as_view()), name='visualizar_restaurante'),
    path('restaurante/<int:restaurante_pk>/avaliacao/<int:pk>/editar', login_required(views.AvaliacaoUpdateView.as_view()), name='editar_avaliacao'),
    path('restaurante/<int:restaurante_pk>/avaliacao/<int:pk>/deletar', login_required(views.AvaliacaoDeleteView.as_view()), name='deletar_avaliacao'),
    path('perfil/', login_required(views.PerfilDetailView.as_view()), name='visualizar_perfil'),
    path('perfil/editar', login_required(views.PerfilUpdateView.as_view()), name='editar_perfil'),
    path('cozinhas/', login_required(views.CozinhasView.as_view()), name='cozinhas'),
    path('mapa/', login_required(views.MapaDoSiteView.as_view()), name='mapa'),
    path('perguntas_frequentes/', login_required(views.PerguntasFrequentesView.as_view()), name='perguntas_frequentes'),
    path('acessibilidade/', login_required(views.AcessibilidadeView.as_view()), name='acessibilidade'),
    path('incluir_estabelecimento/', login_required(views.IncluirEstabelecimentoView.as_view()), name='incluir_estabelecimento'),
    re_path(r'^contato/(?P<tipo>((sugestao)|(duvida)|(reclamacao))){0,1}$', login_required(views.MensagemContatoCreateView.as_view()), name='enviar_mensagem'),
    path('missao/', login_required(views.MissaoView.as_view()), name='missao'),
    path('financas/', login_required(views.FinancasView.as_view()), name='financas'),
    path('trabalhe_conosco/', login_required(views.TrabalheConoscoView.as_view()), name='trabalhe_conosco'),
    path('eventos/', login_required(views.EventosView.as_view()), name='eventos'),
    path('itemLog/', login_required(views.MensagemContatoCreateView.as_view()), name='log'),
    path('entrar', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair', auth_views.LogoutView.as_view(), name='logout'),
]
