import math

"""
Esse script lê um ângulo qualquer e mostra na tela o valor do seno, cosseno
tangente desse ângulo.
"""


angulo = float(input('Informe um ângulo qualquer: '))
print('Seno: {}'.format(math.sin(angulo)))
print('Cosseno: {}'.format(math.cos(angulo)))
print('Tangente: {}'.format(math.tan(angulo)))
