from django.db import models
from django.conf import settings

class Acao(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    rota = models.TextField(null=False)
    parametros_get = models.TextField(null=False)
    parametros_post = models.TextField(null=False)

    def __str__(self):
        return str(self.usuario) + " em " + str(self.rota) + " (" + str(self.data) + "). GET: " + self.parametros_get + " POST: " + self.parametros_post

    class Meta:
        verbose_name_plural = 'Ações'
        verbose_name = 'Ação'
        db_table = 'Acao'