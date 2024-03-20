"""
Esse programa lê um número e mostra na tela se é par ou ímpar.
"""


num = int(input('Digite um número: '))

if num % 2 == 0:
    print('{} é um número par.'.format(num))
else:
    print('{} é um número ímpar.'.format(num))
