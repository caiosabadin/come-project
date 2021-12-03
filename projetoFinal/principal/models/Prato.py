from django.db import models

class Prato(models.Model):

    nome = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Prato'
        ordering = ['nome']