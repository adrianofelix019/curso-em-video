def leia_int(msg):
    while True:
        valor = input(msg)

        if valor.isdigit():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[0m')


print('-' * 50)
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
