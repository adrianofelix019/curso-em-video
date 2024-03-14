from math import trunc

"""
Esse script lê um número pelo teclado e exibi sua porção inteira.
"""

num = float(input('Informe um número: '))
print('A porção inteira de {} é {}'.format(num, trunc(num)))
