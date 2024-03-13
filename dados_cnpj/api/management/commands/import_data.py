from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import wget
import zipfile
import urllib3
import os

class Command(BaseCommand):
    help = 'Baixa e extrai os arquivos .zip de https://dadosabertos.rfb.gov.br/CNPJ/'

    def handle(self, *args, **kwargs):
        url = 'https://dadosabertos.rfb.gov.br/CNPJ/'
        destino = os.path.join(os.getcwd(), 'api', 'arquivos_csv')

        if not os.path.exists(destino):
            os.makedirs(destino)

        conexao = urllib3.PoolManager()
        retorno = conexao.request('GET', url)
        pagina = BeautifulSoup(retorno.data, 'html.parser')
        links = []

        for link in pagina.find_all('a'):
            href = link.get('href')
            if href.endswith('.zip'):
                links.append(url + href)

        for link in links:
            wget.download(link, destino)
        
        for link in links:
            arquivo_zip = os.path.join(destino, link[37:])
            arquivo_csv = os.path.join(destino, link[37:].split('.')[0] + '.csv')
            with zipfile.ZipFile(arquivo_zip, 'r') as zip:
                zip.extract(arquivo_csv)
                os.remove(arquivo_zip)


        