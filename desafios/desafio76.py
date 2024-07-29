listagem = ('Notebook', 3499, 'Celular', 1899, 'XBox', 4379, 'Playstation 5', 3199, 'Controle', 199.90)
print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
