from random import randint


print('-='*15)
print(f'{"JOGOS DA MEGASENA":^30}')
print('-='*15)

num_jogos = int(input('Quanto jogos quer gerar? '))
jogos = []

for c in range(num_jogos):
    jogo = []
    for i in range(6):
        jogo.append(randint(1, 60))
    jogos.append(jogo[:])

print('Os jogos gerados foram:')
for indice, jogo in enumerate(jogos):
    print(f'Jogo {indice+1}: ', end='')
    for indice, numero in enumerate(jogo):
        print(f'{numero:>3}', end=', ' if indice != len(jogo) - 1 else '\n')
