from lib.dados import leia_int


def linha(tamanho=42):
    print('-' * tamanho)


def cabecalho(texto):
    linha()
    print(f'{texto.upper().center(42)}')
    linha()


def menu(opcoes):
    for i, opcao in enumerate(opcoes):
        print(f'[{i + 1}] - {opcao}')
    linha()
    resposta = leia_int('Opção: ')
    return resposta
