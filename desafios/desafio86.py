matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite o valor [{linha}, {coluna}]: '))
        matriz[linha].append(valor)

print('-='*30)

for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print('')
