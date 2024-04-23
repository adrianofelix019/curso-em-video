'''
Esse programa lê um número inteiro e mostra na tela se ele é ou não um número
primo.
'''

n = int(input('Informe um número para verificar se ele é primo: '))

e_primo = True
divisores = 0

for c in range(1, n + 1):

    if n % c == 0:
        divisores += 1
        print('\033[92m{}\033[0m'.format(c), end=' ')
    else:
        print('\033[91m{}\033[0m'.format(c), end=' ')

print('\nO número {} é divisível por {} números'.format(n, divisores))
print('E por isso ele ', end='')

if divisores == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')
