from django.db import models
from django.utils import timezone


# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=False)
    autores = models.CharField(max_length=300, blank=False, null=False)
    resumo = models.TextField(blank=False, null=False)
    abstract = models.TextField(blank=False, null=False)
    palavras_chave = models.CharField(max_length=200, blank=False, null=False)
    data_ano = models.IntegerField(blank=False, null=False, default=timezone.now().year)
    revista = models.CharField(max_length=200, blank=False, null=False)
    arquivo = models.FileField(upload_to='uploads/', blank=False)
    data_ultima_edicao = models.DateTimeField(auto_now=True)

