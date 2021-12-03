from principal.models import Acao
import re

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            copia_get = request.GET.copy()
            copia_post = request.POST.copy()
            # Remove o token de segurança de aparecer no log
            if 'csrfmiddlewaretoken' in copia_post:
                copia_post.pop('csrfmiddlewaretoken')
            # Remove a senha de aparecer no log
            if 'password' in copia_post:
                copia_post.pop('password')
            # Remove imagens e caminhos da seção administrativa do Django do log
            if (re.search('(\.jpg|\.png|\.jpeg|\.ico)$', request.path) == None) and (re.search('\/ctrl\/', request.path) == None):
                acao = Acao(usuario=request.user, rota=request.path, parametros_get=str(copia_get.dict()), parametros_post=str(copia_post.dict()))
                acao.save()
        return response
        