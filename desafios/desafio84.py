pessoas = []
dados = []
maior_peso = 0
menor_peso = 0
nomes_maior_peso = []
nomes_menor_peso = []

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Continuar? [S/N] ').strip().lower()[0]
    if continuar == 'n':
        break

for indice, pessoa in enumerate(pessoas):
    nome = pessoa[0]
    peso = pessoa[1]

    if indice == 0:
        maior_peso = peso
        menor_peso = peso
    
    if peso > maior_peso:
        maior_peso = peso
    
    if peso < menor_peso:
        menor_peso = peso

print('-='*25)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(pessoa[0], end=', ')

print('')

print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(pessoa[0], end=', ')
