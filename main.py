import requests
from biblioteca import *


usuario = input("Digite o usuario do repositório: ")
repositorio = input("Digite o repositório: ")

print(pega_valor_da_versao_do_repo(usuario, repositorio))

dados = pega_valor_da_versao_do_repo(usuario, repositorio)

banco_existe_senao_crie('dados_repo')

guardar_dados('dados repo', dados)







