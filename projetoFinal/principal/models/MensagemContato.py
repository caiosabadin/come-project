from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class MensagemContato(models.Model):

    TIPOS_CONTATO = (
        (1, 'Sugestão'),
        (2, 'Dúvida'),
        (3, 'Reclamação'),
        (4, 'Outros'),
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=False)
    tipo_contato = models.PositiveSmallIntegerField(choices=TIPOS_CONTATO, default=None, blank=False, null=False)
    mensagem = models.TextField(validators=[MinLengthValidator(25, message='Sua mensagem de contato precisa ter no mínimo 25 caracteres')], blank=False, null=False)
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        formas_contato = {k: v for k, v in self.TIPOS_CONTATO}
        forma_contato = formas_contato[self.tipo_contato]
        return forma_contato + " de " + str(self.usuario) + ":\n" + self.mensagem

    class Meta:
        ordering = ['data', 'tipo_contato']
        verbose_name_plural = 'Mensagens de contato'
        verbose_name = 'Mensagem de contato'
        db_table = 'Mensagem_Contato'