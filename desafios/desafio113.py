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


def leiaFloat(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número real válido.\033[0m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[0m')
            return 0
        else:
            return valor


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real:.1f}')
