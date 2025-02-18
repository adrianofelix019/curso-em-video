valores = []
indice_para_inserção = 0

for c in range(5):
    valor = int(input('Digite um valor: '))

    if not valores or valor > max(valores):
        valores.append(valor)
        print(f'{valor} foi inserido no final da lista.')
    else:
        for indice, valor_da_lista in enumerate(valores):
            if valor < valor_da_lista:
                indice_para_inserção = indice
                break
        valores.insert(indice, valor)
        print(f'O valor {valor} foi inserido no indice {indice}')

print('-='*30)
print(f'Os valores digitados em ordem foram: {valores}')
