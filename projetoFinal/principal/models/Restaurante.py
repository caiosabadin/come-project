from django.db import models
from .Prato import Prato
from .Endereco import Endereco
from .Imagem import Imagem

class Restaurante(models.Model):

    nome = models.CharField(max_length=255, blank=False, null=False)
    endereco = models.ForeignKey(Endereco, verbose_name="Endereço", on_delete=models.SET_NULL, null=True)
    sobre = models.TextField(max_length=320, blank=False, null=False)
    fotos = models.ManyToManyField(Imagem, limit_choices_to={'is_foto_perfil': False}, blank=True)
    pratos = models.ManyToManyField(Prato, verbose_name="Pratos principais")

    def __str__(self):
        return self.nome + " (" + str(self.endereco) + ")"
        
    class Meta:
        db_table = 'Restaurante'
        ordering = ['endereco', 'nome']