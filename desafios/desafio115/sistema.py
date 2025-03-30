from lib import interface
from lib.arquivo import arquivo_existe, criar_arquivo, ler_arquivo
from time import sleep

NOME_ARQUIVO = 'banco_de_dados.txt'


if not arquivo_existe(NOME_ARQUIVO):
    criar_arquivo(NOME_ARQUIVO)

while True:
    
    interface.cabecalho('sistema arquivo v1.0')
    resposta = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        ler_arquivo(NOME_ARQUIVO)
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        interface.cabecalho('Saindo do Sistema... Até logo.')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
        sleep(2)
