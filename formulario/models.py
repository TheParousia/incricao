from django.db import models

# Create your models here.
class InscritoPernoite(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    vai_calebe = models.BooleanField(default=True)
    usercodeUsado = models.CharField(max_length=100, blank=True, null=True)
    ip_usado = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"