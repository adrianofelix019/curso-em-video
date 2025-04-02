def leia_int(mensagem):
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


def nome_valido(nome):
    for letra in nome:
        if letra.isalpha() or letra.isspace():
            continue
        else:
            return False
    return True


def leia_nome(mensagem):
    while True:
        try:
            nome = str(input(mensagem))
            if nome_valido(nome):
                return nome
            else:
                print('\033[31mPor favor, informe um nome válido.\033[0m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[0m')
            return 'Anônimo'


def cadastrar_pessoa():
    from lib.interface import cabecalho


    cabecalho('cadastrar nova pessoa')

    try:
        nome = leia_nome('Nome: ')
        idade = leia_int('Idade: ')
    except KeyboardInterrupt:
        print('O usuário interrompeu o cadastro.')
    else:
        return { 'nome': nome, 'idade': idade } 
