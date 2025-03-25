def ficha(nome, qtd_gols):
    if nome == '':
        nome = '<desconhecido>'
    
    if qtd_gols == '':
        qtd_gols = 0
    else:
        qtd_gols = int(qtd_gols)

    print(f'O jogador {nome} fez {qtd_gols} gol(s) no campeonato')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(nome, gols)
