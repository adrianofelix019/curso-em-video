from time import sleep


def py_help():
    verde = '\033[32m'
    limpa = '\033[m'
    preto = '\033[30m'
    fundo_branco = '\033[47m'

    while True:
        print(f'{verde}', '-' * 50, f'{limpa}')
        print(f'{verde}{"SISTEMA DE AJUDA PY HELP":^50}{limpa}')
        print(f'{verde}', '-' * 50, f'{limpa}')
        comando = input('Função ou biblioteca > ').strip().lower()

        if comando == 'sair':
            break

        print(f'Acessando a documentação de \'{comando}\'...')
        sleep(0.5)

        print(preto)
        print(fundo_branco)
        help(comando)
        print(limpa)
        
    print('-' * 50)
    print('Saindo...')
    sleep(0.5)

py_help()
