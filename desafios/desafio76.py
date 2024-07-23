listagem = ('Notebook', 3499, 'Celular', 1899, 'XBox', 4379, 'Playstation 5', 3199, 'Controle', 199.90)
print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)
for i in range(0, len(listagem), 2):
    if i == len(listagem) - 1:
        break
    print(f'{listagem[i]:.<40}R${listagem[i+1]: >10.2f}')
