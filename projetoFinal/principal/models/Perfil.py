from django.db import models
from django.conf import settings
from django.utils.timesince import timesince
from .Prato import Prato
from .Imagem import Imagem
from .Frase import Frase
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

class Perfil(models.Model):

    GRUPOS = (
        ('C', 'Grupo de Controle'),
        ('E', 'Grupo Experimental')
    )

    CULINARIAS_FAVORITAS = (
        (None, 'Escolha sua culinária favorita nesta lista'),
        (1, 'Árabe'),
        (2, 'Brasileira'),
        (3, 'Chinesa'),
        (4, 'Indiana'),
        (5, 'Italiana'),
        (6, 'Japonesa'),
        (7, 'Mexicana'),
    )

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='perfil', on_delete=models.SET_NULL, null=True)
    nome_fantasia = models.CharField(max_length=50, default='João Silva', blank=False, null=False)
    foto_fantasia = models.ForeignKey(Imagem, limit_choices_to={'is_foto_perfil': True}, blank=False, null=True, on_delete=models.SET_NULL)
    prato_preferido = models.ForeignKey(Prato, default=None, on_delete=models.SET_NULL, null=True, blank=False)
    grupo = models.CharField(max_length=1, choices=GRUPOS, blank=True, null=True)
    frase_bio = models.ForeignKey(Frase, default=1, on_delete=models.SET_NULL, null=True, blank=False)
    data_nascimento_fantasia = models.CharField(max_length=10, validators=[RegexValidator(regex='^21\.11\.(20)?27$', message='Por favor, digite a data solicitada usando apenas números, e use um ponto para separar o dia do mês e o mês do ano.')], default=None, blank=True, null=True)
    culinaria_favorita_fantasia = models.PositiveSmallIntegerField(choices=CULINARIAS_FAVORITAS, validators=[MinValueValidator(5, message='Por favor, escolha a culinária italiana'), MaxValueValidator(5, message='Por favor, escolha a culinária italiana')], default=None, null=True, blank=True)

    def __str__(self):
        return str(self.nome_fantasia) + " (" + str(self.grupo) + "), " + str(self.prato_preferido)

    @property
    def cadastrado_ha(self):
        return timesince(self.usuario.date_joined).split(',', 1)[0]

    class Meta:
        verbose_name_plural = 'Perfis'
        db_table = 'Perfil'