from django.db import models

class Frase(models.Model):
    texto = models.CharField(max_length=255, blank=False, null=False)
    autor = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.autor

    class Meta:
        ordering = ['autor']
        db_table = 'Frase'