from django.core.management.base import BaseCommand
from api.models import *

class Command(BaseCommand):
    help = 'Salva dados no Banco de Dados.'

    def handle(self, *args, **kwargs):
        Cnaes.salvar_dados()
        Motivos.salvar_dados()
        Municipios.salvar_dados()
        Naturezas.salvar_dados()
        Paises.salvar_dados()
        Qualificacoes.salvar_dados()
        Empresas.salvar_dados()
        Estabelecimentos.salvar_dados()
        Socios.salvar_dados()
        Simples.salvar_dados()
