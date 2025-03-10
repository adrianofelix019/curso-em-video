from random import randint
from time import sleep
import operator

jogadores = dict()

print('Valores sorteados:')
for c in range(4):
    dado = randint(1, 6)
    chave = f'jogador{c + 1}'
    sleep(0.5)
    print(f'\tO {chave} tirou {dado}')
    jogadores[chave] = dado

jogadores_ordenado = dict(sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True))

print('Ranking dos jogadores:')
c = 1
for k, v in jogadores_ordenado.items():
    print(f'\t{c}° lugar: {k} com {v}')
    c += 1
    sleep(0.5)
