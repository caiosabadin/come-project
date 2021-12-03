from django.db import models

class Imagem(models.Model):
    titulo = models.CharField(max_length=145, null=True, blank=True, verbose_name='Título')
    descricao = models.TextField(null=False, blank=False, verbose_name='Descrição')
    descricao_experimental = models.TextField(null=True, blank=True, verbose_name='Descrição (para o grupo experimental)')
    caption = models.CharField(max_length=255, null=True, blank=True, verbose_name='Legenda da figura')
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    endereco = models.ImageField(null=False, blank=False, verbose_name="Endereço")
    is_foto_perfil = models.BooleanField(default=False, null=False, blank=False, verbose_name="Foto de perfil")

    def __str__(self):
        return str(self.titulo) + ' (' + str(self.endereco) + '): ' + str(self.descricao)

    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Imagens'
        db_table = 'Imagem'