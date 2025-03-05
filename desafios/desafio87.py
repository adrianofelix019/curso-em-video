matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

for linha in range(3):
    for coluna in range(3):
        num = int(input(f'Digite o valor [{linha}, {coluna}]: '))
        matriz[linha].append(num)

        if num % 2 == 0:
            soma_pares += num
        
        if coluna == 2:
            soma_terceira_coluna += num


print('-='*30)

for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print('')

print('-='*30)
print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma da terceira coluna: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
