import os
from lib.interface import cabecalho


def arquivo_existe(nome_arquivo):
    return os.path.exists(nome_arquivo)


def criar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except Exception:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo \'{nome_arquivo}\' criado com sucesso.')


def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
    except Exception:
        print(f'Não foi possível ler o arquivo "{nome_arquivo}".')
    else:
        cabecalho('pessoas cadastradas')
        print(arquivo.readlines())
