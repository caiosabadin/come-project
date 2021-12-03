from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

class Endereco(models.Model):

    LISTA_CIDADES = (
        ('PR', 'Curitiba'),
        ('RJ', 'Rio de Janeiro'),
        ('MG', 'Belo Horizonte'),
        ('SP', 'São Paulo')
    )
    
    logradouro = models.CharField(max_length=255, blank=False, null=False)
    numero = models.PositiveSmallIntegerField(verbose_name="Número", blank=False, null=False)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=False, null=False)
    estado = models.CharField(max_length=255, choices=LISTA_CIDADES, blank=False, null=False)
    cep = models.CharField(max_length=9, validators=[RegexValidator("[0-9]{5}\-[0-9]{3}", "Por favor, informe um CEP no formato NNNNN-NNN.")], default="00000-000", blank=False, null=False)

    def __str__(self):
        cidades = {k: v for k, v in self.LISTA_CIDADES}
        cidade = cidades[self.estado]
        numero = str(self.numero) if self.numero > 0 else "S/N"
        if self.complemento == None:
            return self.logradouro + ", " + numero + ", " + self.bairro + ", " + cidade + " - " + self.estado + " (" + self.cep + ")"
        else:
            return self.logradouro + ", " + numero + ", " + self.complemento + ", " + self.bairro + ", " + cidade + " - " + self.estado + " (" + self.cep + ")"

    class Meta:
        ordering = ['estado', 'logradouro']
        verbose_name = 'Endereço'
        db_table = 'Endereco'