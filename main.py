import requests
from biblioteca import *

repositorio = "https://github.com/pixies/calculadora-teste-py/releases/latest"
arquivo_teste = "teste.txt"

url = divide_url((pega_versao(repositorio)))

usuario = url[3]
repositorio_ = url[4]
ultima_versao = url[len(url)-1]

print("URL =", repositorio)
print("Nome de Usuário =", usuario)
print("Nome do Projeto =", repositorio_)
print("Última Versão =", ultima_versao)

salvar = ["REPO:", usuario + '/' + repositorio_, "VERSION:", ultima_versao]
cria_arquivo(arquivo_teste)
add_arquivo(arquivo_teste, str(salvar))
print(read_arquivo(arquivo_teste))




