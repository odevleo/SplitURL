import requests


def pega_valor_da_versao_do_repo(usuario,repositorio):
    url = 'https://github.com/'+ usuario + '/'+ repositorio+ '/releases/latest'
    req = requests.get(url).url.split('https://')[1]
    host, usuario, repositorio, releases, tag, versao = req.split('/')
    return {'host': host, 'usuario': usuario, 'repositorio': repositorio
    ,'versao': versao}



def banco_existe_senao_crie(nome_banco):

    return open(nome_banco, 'a')


def guardar_dados(nome_banco, dados):
    arq = banco_existe_senao_crie(nome_banco)
    arq.write(dados)
    arq.close()
    pass