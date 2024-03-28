import random
from time import sleep

"""
Esse programa joga JO-KEN-PO com você.
"""
itens = ('pedra', 'papel', 'tesoura')

print("Vamos jogar Jokenpô!")
jogador_input = int(input("""Você vai jogar:
[1] - Pedra
[2] - Papel
[3] - Tesoura
"""))
jogador = itens[jogador_input - 1] # -1 para evitar IndexError
computador = itens[random.randint(0, 2)]
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print(f'O computador escolheu {computador}')
sleep(1)
print(f'O jogador escolheu {jogador}')

if jogador == computador:
    print("Empate!")
elif (computador == 'pedra' and jogador == 'tesoura') or \
         (computador == 'papel' and jogador == 'pedra') or \
         (computador == 'tesoura' and jogador == 'papel'):
        print("O computador ganhou!")
else:
    print("O jogador ganhou!")
