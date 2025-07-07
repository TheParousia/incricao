from django.db import models

# Create your models here.
class InscritoPernoite(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    vai_calebe = models.BooleanField(default=True)
    camisa_calebe = models.BooleanField(default=True)
    datas_disponiveis = models.CharField(max_length=255, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    usercode_usado = models.ForeignKey('LinkCode', on_delete=models.SET_NULL, blank=True, null=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    ip_usado = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
    
class LinkCode(models.Model):
    usercode = models.CharField(max_length=100, unique=True)
    observacao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_expiracao = models.DateTimeField()

    def __str__(self):
        return self.usercode

    class Meta:
        verbose_name = "Link Code"
        verbose_name_plural = "Link Codes"