from django.db import models
import hashlib

class Arquivo(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    hash = models.CharField(max_length=64)
    data_ultima_modificacao = models.DateTimeField(auto_now=True)

    def calcular_hash_e_salvar(self, arquivo):
        sha256_hash = hashlib.sha256()
        # Calcular hash do arquivo


class Empresas(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    razao_social = models.CharField(max_width=255)
    natureza_juridica = models.CharField(max_length=4)
    qualificacao_do_responsavel = models.CharField()
    capital_social_da_empresa = models.CharField()
    porte_da_empresa = models.CharField(max_length=2)
    ente_federativo_responsavel = models.CharField()


class Estabelecimentos(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    cnpj_ordem = models.CharField()
    cnpj_dv = models.CharField(max_length=2)
    identificador_matriz_filial = models.CharField(max_length=1)
    nome_fantasia = models.CharField(max_length=255)
    situacao_cadastral = models.CharField(max_length=2)
    motivo_situacao_cadastral = models.CharField(max_length=2)
    nome_da_cidade_no_exterior = models.CharField()
    pais = models.CharField(max_length=3)
    data_de_inicio_atividade = models.CharField()
    cnae_fiscal_principal = models.CharField()
    cnae_fiscal_secundaria = models.CharField()
    tipo_de_logradouro = models.CharField()
    logradouro = models.CharField()
    numero = models.CharField()
    complemento = models.CharField()
    bairro = models.CharField()
    cep = models.CharField()
    uf = models.CharField()
    municipio = models.CharField(max_length=4)
    ddd_1 = models.CharField()
    telefone_1 = models.CharField()
    ddd_2 = models.CharField()
    telefone_2 = models.CharField()
    ddd_do_fax = models.CharField()
    fax = models.CharField()
    correio_eletronico = models.CharField()
    situacao_especial = models.CharField()
    data_da_situacao_especial = models.CharField()


class Simples(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    opcao_pelo_simples = models.CharField()
    data_de_opcao_pelo_simples = models.CharField()
    data_de_exclusao_do_simples = models.CharField()
    opcao_pelo_mei = models.CharField()
    data_de_opcao_pelo_mei = models.CharField()
    data_de_exclusao_do_mei = models.CharField()


class Socios(models.Model):
    cnpj_basico = models.CharField(max_length=8, primary_key=True)
    identificador_de_socio = models.CharField()
    nome_do_socio_razao_social = models.CharField(max_length=255)
    cnpj_cpf_do_socio = models.CharField()
    qualificacao_do_socio = models.CharField()
    data_de_entrada_sociedade = models.CharField()
    pais = models.CharField(max_length=3)
    representante_legal = models.CharField()
    nome_do_representante = models.CharField()
    qualificacao_do_representante_legal = models.CharField()
    faixa_etaria = models.CharField()


class Cnaes(models.Model):
    codigo = models.CharField(max_length=7, primary_key=True)
    descricao = models.CharField(max_length=200)


class Motivos(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    descricao = models.CharField(max_length=100)


class Municipios(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    descricao = models.CharField(max_length=40)


class Naturezas(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    descricao = models.CharField(max_length=100)


class Paises(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    descricao = models.CharField(max_length=50)


class Qualificacoes(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    descricao = models.CharField(max_length=100)
