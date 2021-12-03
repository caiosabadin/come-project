from django.db import models
from django.conf import settings
from .Restaurante import Restaurante
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Avaliacao(models.Model):

    NOTAS_POSSIVEIS = (
        (1, 'Nota 1'),
        (2, 'Nota 2'),
        (3, 'Nota 3'),
        (4, 'Nota 4'),
        (5, 'Nota 5'),
    )

    nota = models.PositiveSmallIntegerField(choices=NOTAS_POSSIVEIS, default=None, blank=False, null=False)
    texto = models.CharField(max_length=100, validators=[MaxLengthValidator(100, message='O texto de sua avaliação pode ter somente até 100 caracteres'), MinLengthValidator(10, message='O texto de sua avaliação precisa ter no mínimo 10 caracteres')], blank=False, null=False)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    restaurante = models.ForeignKey(Restaurante, related_name='avaliacoes', on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.autor) + ' (' + self.data.strftime("%d/%m/%Y") + '): "' + self.texto + '", ' + str(self.nota) + '/5'

    class Meta:
        unique_together = ('autor', 'restaurante')
        verbose_name_plural = 'Avaliações'
        verbose_name = 'Avaliação'
        db_table = 'Avaliacao'