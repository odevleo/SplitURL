import requests

def pega_versao(link):
    url = requests.get(link).url
    return url


def divide_url(split_url):
    url_dividida = split_url.split('/')
    return url_dividida


def arquivo_existe(nome_do_arquivo):
    try:
        open(nome_do_arquivo, 'r')
        return True
    except:
        return False



def cria_arquivo(nome_do_arquivo):
    if not arquivo_existe(nome_do_arquivo):
        arquivo = open(nome_do_arquivo, 'w')
        arquivo.write("")
        arquivo.close()


def read_arquivo(nome_do_arquivo):
    if arquivo_existe(nome_do_arquivo):
        arquivo = open(nome_do_arquivo, 'r')
        return arquivo.read()
    else:
        return "Arquivo não existe."



def add_arquivo(nome_do_arquivo, dados):
    if arquivo_existe(nome_do_arquivo):
        arquivo = open(nome_do_arquivo, 'a')
        arquivo.write(dados + "\n")
        arquivo.close()
    else:
        return "Arquivo não existe."