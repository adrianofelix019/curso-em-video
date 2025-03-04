pessoas = []
dados = []
maior_peso = menor_peso = 0
nomes_maior_peso = []
nomes_menor_peso = []

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Continuar? [S/N] ').strip().lower()[0]
    if continuar == 'n':
        break

print('-='*25)
print(f'Os dados foram {pessoas}')
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}] ', end='')

print('')

print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')
