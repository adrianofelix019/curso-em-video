"""
Esse programa lê um número entre 0 e 9999 e mostra na tela cada um dos digitos
separados.

Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

num = input('Digite um número: ')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
