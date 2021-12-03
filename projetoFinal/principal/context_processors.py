from django.conf import settings
from principal.models import Perfil
from django.conf import settings

def perfil_usuario(request):
    if request.user.is_authenticated:
        return {
            "perfil_usuario": Perfil.objects.get(usuario=request.user.id),
        }
    else:
        return {
            "perfil_usuario": None,
        }