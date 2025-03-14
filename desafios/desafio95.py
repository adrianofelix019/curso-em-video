jogadores = []

while True:
    print('-'*50)
    nome = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols = []
    for i in range(partidas):
        g = int(input(f'Quantos gols na {i+1}° partida? '))
        gols.append(g)
    
    jogador = {
        'nome': nome,
        'gols': gols,
        'total': sum(gols)
    }

    jogadores.append(jogador)

    continuar = input('Continuar? [S/N] ').strip().lower()[0]
    if continuar == 'n':
        break

print(f'{"COD":<5}{"NOME":<20}{"GOLS":<10}{"TOTAL"}')
print('-'*40)
for indice, jogador in enumerate(jogadores):
    print(f'{indice:<3}{jogador["nome"]:<20}{str(jogador["gols"]):<10}{jogador["total"]:>3}')

while True:
    consulta = int(input('Mostrar dados de qual jogador? (999 para sair) '))

    if consulta >= 0 and consulta < len(jogadores):
        j = jogadores[consulta]
        print(f'Levantamento do jogador {j['nome']}:')
        for c, jog in enumerate(j['gols']):
            print(f'\tNa partida {c+1} ele fez {jog} gols.')
    print('-'*40)

    if consulta == 999:
        break
