nome = input('Nome do jogador: ')
gols = []
qtd_partidas = int(input(f'Quantas partidas {nome} jogou? '))
jogador = {
    'nome': nome,
}

for partida in range(qtd_partidas):
    g = int(input(f'Quantos gols na {partida+1}° partida? '))
    gols.append(g)

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-='*25)
print(jogador)
print('-='*25)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-='*25)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
for indice, g in enumerate(jogador['gols']):
    print(f'\tNa partida {indice+1}, fez {g} gols.')
print(f'Foi um total de {jogador['total']} gols.')
