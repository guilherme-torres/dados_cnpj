from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import zipfile
import os
import tqdm

class Command(BaseCommand):
    help = 'Baixa e extrai os arquivos .zip de https://dadosabertos.rfb.gov.br/CNPJ/'

    def handle(self, *args, **kwargs):
        url = 'https://dadosabertos.rfb.gov.br/CNPJ/'
        destino = os.path.join(os.getcwd(), 'api', 'arquivos_csv')

        if not os.path.exists(destino):
            os.makedirs(destino)

        resposta = requests.get(url)
        pagina = BeautifulSoup(resposta.content, 'html.parser')
        links = []

        for link in pagina.find_all('a'):
            href = link.get('href')
            if href.endswith('.zip'):
                links.append(url + href)
        
        for link in links:
            resposta = requests.get(link, stream=True)
            arquivo_zip = os.path.join(destino, link[37:])
            if resposta.status_code == requests.codes.OK:
                with open(arquivo_zip, 'wb') as arquivo:
                    total = int(resposta.headers.get('content-length', 0))
                    tqdm_params = {
                        'desc': link,
                        'total': total,
                        'miniters': 1,
                        'unit': 'B',
                        'unit_scale': True,
                        'unit_divisor': 1024,
                    }
                    with tqdm.tqdm(**tqdm_params) as pb:
                        for chunk in resposta.iter_content(chunk_size=1024*10):
                            pb.update(len(chunk))
                            arquivo.write(chunk)
            else:
                resposta.raise_for_status()

        for link in links:
            arquivo_zip = os.path.join(destino, link[37:])
            # arquivo_csv = os.path.join(destino, link[37:].split('.')[0] + '.csv')
            with zipfile.ZipFile(arquivo_zip, 'r') as zip:
                zip.extract(destino)
            os.remove(arquivo_zip)
