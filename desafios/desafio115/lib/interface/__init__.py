def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro válido.\033[0m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[0m')
            return 0
        else:
            return valor




def linha(tamanho=42):
    print('-' * tamanho)


def cabecalho(texto):
    linha(len(texto) + 4)
    print(f'  {texto.upper()}')
    linha(len(texto) + 4)


def menu(opcoes):
    for i, opcao in enumerate(opcoes):
        print(f'[{i + 1}] - {opcao}')
    linha(24)
    resposta = leiaInt('Opção: ')
    return resposta
