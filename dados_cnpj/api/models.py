from django.db import models
import hashlib

class Arquivo(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    hash = models.CharField(max_length=64)
    data_ultima_modificacao = models.DateTimeField(auto_now=True)

    def calcular_hash_e_salvar(self, arquivo):
        sha256_hash = hashlib.sha256()
        # Calcular hash do arquivo