import random

"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

print("Vamos jogar Jokenpô!")
jogador = input("""Você vai jogar:
[1] - Pedra
[2] - Papel
[3] - Tesoura
""")
computador = random.randint(1, 3)

if jogador == computador:
    print("Empate!")
elif (computador == 'pedra' and jogador == 'tesoura') or \
         (computador == 'papel' and jogador == 'pedra') or \
         (computador == 'tesoura' and jogador == 'papel'):
        print("O computador ganhou!")
else:
    print("Você ganhou!")
