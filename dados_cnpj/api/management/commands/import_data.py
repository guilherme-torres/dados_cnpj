from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import zipfile
import urllib
import os

class Command(BaseCommand):
    help = 'Baixa e extrai os arquivos .zip de https://dadosabertos.rfb.gov.br/CNPJ/'

    def handle(self, *args, **kwargs):
        url = 'https://dadosabertos.rfb.gov.br/CNPJ/'
        output_folder = 'api/dados_csv/'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href.endswith('.zip'):
                    full_url = urllib.parse.urljoin(url, href)
                    file_name = os.path.join(output_folder, href)
                    response = requests.get(full_url)
                    with open(file_name, 'wb') as f:
                        f.write(response.content)

                    with zipfile.ZipFile(file_name, 'r') as zip_ref:
                        zip_ref.extractall(output_folder)

                    os.remove(file_name)