from django.db import models
# import hashlib
import os
import csv

# class Arquivo(models.Model):
#     nome = models.CharField(max_length=255, unique=True)
#     hash = models.CharField(max_length=64)
#     data_ultima_modificacao = models.DateTimeField(auto_now=True)

#     def calcular_hash_e_salvar(self, arquivo):
#         sha256_hash = hashlib.sha256()
#         # Calcular hash do arquivo


class Empresas(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    razao_social = models.CharField(max_length=255)
    natureza_juridica = models.CharField(max_length=4)
    qualificacao_do_responsavel = models.CharField(max_length=2)
    capital_social_da_empresa = models.CharField(max_length=11)
    porte_da_empresa = models.CharField(max_length=2)
    ente_federativo_responsavel = models.CharField(max_length=100)
    
    @staticmethod
    def salvar_dados():
        csv_dir = os.path.join(os.getcwd(), 'api', 'dados', 'csv')
        arquivos_empresas = [os.path.join(csv_dir, arquivo) for arquivo in os.listdir(csv_dir) if arquivo.startswith('Empresas')]
        fieldnames = [
            'cnpj_basico', 'razao_social', 'natureza_juridica', 'qualificacao_do_responsavel',
            'capital_social_da_empresa', 'porte_da_empresa', 'ente_federativo_responsavel'
        ]
        for arquivo_empresas in arquivos_empresas:
            with open(arquivo_empresas, encoding='ISO-8859-1') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
                for row in reader:
                    empresas = Empresas(
                        cnpj_basico=row['cnpj_basico'],
                        razao_social=row['razao_social'],
                        natureza_juridica=row['natureza_juridica'],
                        qualificacao_do_responsavel=row['qualificacao_do_responsavel'],
                        capital_social_da_empresa=row['capital_social_da_empresa'],
                        porte_da_empresa=row['porte_da_empresa'],
                        ente_federativo_responsavel=row['ente_federativo_responsavel']
                    )
                    empresas.save()


class Estabelecimentos(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    cnpj_ordem = models.CharField(max_length=4)
    cnpj_dv = models.CharField(max_length=2)
    identificador_matriz_filial = models.CharField(max_length=1)
    nome_fantasia = models.CharField(max_length=100)
    situacao_cadastral = models.CharField(max_length=2)
    data_situacao_cadastral = models.CharField(max_length=8)
    motivo_situacao_cadastral = models.CharField(max_length=2)
    nome_da_cidade_no_exterior = models.CharField(max_length=60)
    pais = models.CharField(max_length=3)
    data_de_inicio_atividade = models.CharField(max_length=8)
    cnae_fiscal_principal = models.CharField(max_length=7)
    cnae_fiscal_secundaria = models.CharField(max_length=7)
    tipo_de_logradouro = models.CharField(max_length=12)
    logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=60)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=4)
    ddd_1 = models.CharField(max_length=2)
    telefone_1 = models.CharField(max_length=9)
    ddd_2 = models.CharField(max_length=2)
    telefone_2 = models.CharField(max_length=9)
    ddd_do_fax = models.CharField(max_length=2)
    fax = models.CharField(max_length=9)
    correio_eletronico = models.CharField(max_length=100)
    situacao_especial = models.CharField(max_length=100)
    data_da_situacao_especial = models.CharField(max_length=8)

    @staticmethod
    def salvar_dados():
        csv_dir = os.path.join(os.getcwd(), 'api', 'dados', 'csv')
        arquivos_estabelecimentos = [os.path.join(csv_dir, arquivo) for arquivo in os.listdir(csv_dir) if arquivo.startswith('Estabelecimentos')]
        fieldnames = [
            'cnpj_basico', 'cnpj_ordem', 'cnpj_dv', 'identificador_matriz_filial', 
            'nome_fantasia', 'situacao_cadastral', 'data_situacao_cadastral', 
            'motivo_situacao_cadastral', 'nome_da_cidade_no_exterior', 'pais', 
            'data_de_inicio_atividade', 'cnae_fiscal_principal', 'cnae_fiscal_secundaria', 
            'tipo_de_logradouro', 'logradouro', 'numero', 'complemento', 'bairro', 
            'cep', 'uf', 'municipio', 'ddd_1', 'telefone_1', 'ddd_2', 'telefone_2', 
            'ddd_do_fax', 'fax', 'correio_eletronico', 'situacao_especial', 
            'data_da_situacao_especial'
        ]

        for arquivo_estabelecimentos in arquivos_estabelecimentos:
            with open(arquivo_estabelecimentos, encoding='ISO-8859-1') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
                for row in reader:
                    estabelecimentos = Estabelecimentos(
                        cnpj_basico=row['cnpj_basico'],
                        cnpj_ordem=row['cnpj_ordem'],
                        cnpj_dv=row['cnpj_dv'],
                        identificador_matriz_filial=row['identificador_matriz_filial'],
                        nome_fantasia=row['nome_fantasia'],
                        situacao_cadastral=row['situacao_cadastral'],
                        data_situacao_cadastral=row['data_situacao_cadastral'],
                        motivo_situacao_cadastral=row['motivo_situacao_cadastral'],
                        nome_da_cidade_no_exterior=row['nome_da_cidade_no_exterior'],
                        pais=row['pais'],
                        data_de_inicio_atividade=row['data_de_inicio_atividade'],
                        cnae_fiscal_principal=row['cnae_fiscal_principal'],
                        cnae_fiscal_secundaria=row['cnae_fiscal_secundaria'],
                        tipo_de_logradouro=row['tipo_de_logradouro'],
                        logradouro=row['logradouro'],
                        numero=row['numero'],
                        complemento=row['complemento'],
                        bairro=row['bairro'],
                        cep=row['cep'],
                        uf=row['uf'],
                        municipio=row['municipio'],
                        ddd_1=row['ddd_1'],
                        telefone_1=row['telefone_1'],
                        ddd_2=row['ddd_2'],
                        telefone_2=row['telefone_2'],
                        ddd_do_fax=row['ddd_do_fax'],
                        fax=row['fax'],
                        correio_eletronico=row['correio_eletronico'],
                        situacao_especial=row['situacao_especial'],
                        data_da_situacao_especial=row['data_da_situacao_especial']
                    )
                    estabelecimentos.save()


class Simples(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    opcao_pelo_simples = models.CharField(max_length=1)
    data_de_opcao_pelo_simples = models.CharField(max_length=8)
    data_de_exclusao_do_simples = models.CharField(max_length=8)
    opcao_pelo_mei = models.CharField(max_length=1)
    data_de_opcao_pelo_mei = models.CharField(max_length=8)
    data_de_exclusao_do_mei = models.CharField(max_length=8)

    @staticmethod
    def salvar_dados():
        csv_dir = os.path.join(os.getcwd(), 'api', 'dados', 'csv')
        arquivos_simples = [os.path.join(csv_dir, arquivo) for arquivo in os.listdir(csv_dir) if arquivo.startswith('Simples')]
        fieldnames = [
            'cnpj_basico', 'opcao_pelo_simples', 'data_de_opcao_pelo_simples', 'data_de_exclusao_do_simples',
            'opcao_pelo_mei', 'data_de_opcao_pelo_mei', 'data_de_exclusao_do_mei'
        ]
        for arquivo_simples in arquivos_simples:
            with open(arquivo_simples, encoding='ISO-8859-1') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
                for row in reader:
                    simples = Simples(
                        cnpj_basico=row['cnpj_basico'],
                        opcao_pelo_simples=row['opcao_pelo_simples'],
                        data_de_opcao_pelo_simples=row['data_de_opcao_pelo_simples'],
                        data_de_exclusao_do_simples=row['data_de_exclusao_do_simples'],
                        opcao_pelo_mei=row['opcao_pelo_mei'],
                        data_de_opcao_pelo_mei=row['data_de_opcao_pelo_mei'],
                        data_de_exclusao_do_mei=row['data_de_exclusao_do_mei']
                    )
                    simples.save()


class Socios(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    identificador_de_socio = models.CharField(max_length=1)
    nome_do_socio_razao_social = models.CharField(max_length=100)
    cnpj_cpf_do_socio = models.CharField(max_length=14)
    qualificacao_do_socio = models.CharField(max_length=2)
    data_de_entrada_sociedade = models.CharField(max_length=8)
    pais = models.CharField(max_length=3)
    representante_legal = models.CharField(max_length=11)
    nome_do_representante = models.CharField(max_length=100)
    qualificacao_do_representante_legal = models.CharField(max_length=2)
    faixa_etaria = models.CharField(max_length=1)

    @staticmethod
    def salvar_dados():
        csv_dir = os.path.join(os.getcwd(), 'api', 'dados', 'csv')
        arquivos_socios = [os.path.join(csv_dir, arquivo) for arquivo in os.listdir(csv_dir) if arquivo.startswith('Socios')]
        fieldnames = [
            'cnpj_basico', 'identificador_de_socio', 'nome_do_socio_razao_social', 'cnpj_cpf_do_socio',
            'qualificacao_do_socio', 'data_de_entrada_sociedade', 'pais', 'representante_legal',
            'nome_do_representante', 'qualificacao_do_representante_legal', 'faixa_etaria'
        ]
        for arquivo_socios in arquivos_socios:
            with open(arquivo_socios, encoding='ISO-8859-1') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
                for row in reader:
                    socios = Socios(
                        cnpj_basico=row['cnpj_basico'],
                        identificador_de_socio=row['identificador_de_socio'],
                        nome_do_socio_razao_social=row['nome_do_socio_razao_social'],
                        cnpj_cpf_do_socio=row['cnpj_cpf_do_socio'],
                        qualificacao_do_socio=row['qualificacao_do_socio'],
                        data_de_entrada_sociedade=row['data_de_entrada_sociedade'],
                        pais=row['pais'],
                        representante_legal=row['representante_legal'],
                        nome_do_representante=row['nome_do_representante'],
                        qualificacao_do_representante_legal=row['qualificacao_do_representante_legal'],
                        faixa_etaria=row['faixa_etaria']
                    )
                    socios.save()


class Cnaes(models.Model):
    codigo = models.CharField(max_length=7, primary_key=True)
    descricao = models.CharField(max_length=200)

    @staticmethod
    def salvar_dados():
        path = os.path.join(os.getcwd(), 'api', 'dados', 'csv', 'Cnaes.csv')
        with open(path, encoding='ISO-8859-1') as csvfile:
            fieldnames = ['codigo', 'descricao']
            reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
            for row in reader:
                cnaes = Cnaes(codigo=row['codigo'], descricao=row['descricao'])
                cnaes.save()


class Motivos(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    descricao = models.CharField(max_length=100)

    @staticmethod
    def salvar_dados():
        path = os.path.join(os.getcwd(), 'api', 'dados', 'csv', 'Motivos.csv')
        with open(path, encoding='ISO-8859-1') as csvfile:
            fieldnames = ['codigo', 'descricao']
            reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
            for row in reader:
                motivos = Motivos(codigo=row['codigo'], descricao=row['descricao'])
                motivos.save()


class Municipios(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    descricao = models.CharField(max_length=40)

    @staticmethod
    def salvar_dados():
        path = os.path.join(os.getcwd(), 'api', 'dados', 'csv', 'Municipios.csv')
        with open(path, encoding='ISO-8859-1') as csvfile:
            fieldnames = ['codigo', 'descricao']
            reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
            for row in reader:
                municipios = Municipios(codigo=row['codigo'], descricao=row['descricao'])
                municipios.save()


class Naturezas(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    descricao = models.CharField(max_length=100)

    @staticmethod
    def salvar_dados():
        path = os.path.join(os.getcwd(), 'api', 'dados', 'csv', 'Naturezas.csv')
        with open(path, encoding='ISO-8859-1') as csvfile:
            fieldnames = ['codigo', 'descricao']
            reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
            for row in reader:
                naturezas = Naturezas(codigo=row['codigo'], descricao=row['descricao'])
                naturezas.save()


class Paises(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    descricao = models.CharField(max_length=50)

    @staticmethod
    def salvar_dados():
        path = os.path.join(os.getcwd(), 'api', 'dados', 'csv', 'Paises.csv')
        with open(path, encoding='ISO-8859-1') as csvfile:
            fieldnames = ['codigo', 'descricao']
            reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
            for row in reader:
                paises = Paises(codigo=row['codigo'], descricao=row['descricao'])
                paises.save()


class Qualificacoes(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    descricao = models.CharField(max_length=100)

    @staticmethod
    def salvar_dados():
        path = os.path.join(os.getcwd(), 'api', 'dados', 'csv', 'Qualificacoes.csv')
        with open(path, encoding='ISO-8859-1') as csvfile:
            fieldnames = ['codigo', 'descricao']
            reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
            for row in reader:
                qualificacoes = Qualificacoes(codigo=row['codigo'], descricao=row['descricao'])
                qualificacoes.save()
