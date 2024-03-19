from random import randint

"""
O computador vai "pensar" num número entre 0 e 5 tente advinhar o número.
"""


jogador = int(input('Tente advinhar o número entre 0 e 5: '))
computador = randint(0, 5)
if jogador == computador:
    print('Você acertou, o computador pensou no número {}'.format(computador))
else:
    print('Você errou! O computador pensou no número {}.'.format(computador))
