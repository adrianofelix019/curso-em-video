from random import randint
from time import sleep


print('-='*15)
print(f'{"JOGOS DA MEGASENA":^30}')
print('-='*15)

num_jogos = int(input('Quanto jogos quer gerar? '))
jogos = []

for c in range(num_jogos):
    jogo = []
    contador = 0
    while True:
        if contador == 6:
            jogos.append(jogo[:])
            break
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            contador += 1

print(f'-=-=-=-= SORTEANDO {num_jogos} JOGOS -=-=-=-=')
for indice, jogo in enumerate(jogos):
    print(f'Jogo {indice+1}: ', end='')
    for indice, numero in enumerate(jogo):
        print(f'{numero:>3}', end=', ' if indice != len(jogo) - 1 else '\n')
        sleep(0.1)
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
