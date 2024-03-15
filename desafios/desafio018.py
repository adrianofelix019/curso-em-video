from math import sin, cos, tan, radians

"""
Esse script lê um ângulo qualquer e mostra na tela o valor do seno, cosseno
tangente desse ângulo.
"""


angulo = float(input('Informe um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))
