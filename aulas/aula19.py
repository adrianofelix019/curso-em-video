estado = {}
brasil = []

for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for chave, valor in e.items():
        print(f'O campo {chave} tem o valor {valor}')
