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

num = int(input('Digite um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
