valores = []

for c in range(5):
    valores.append(int(input(f'Digite o valor de indice {c}: ')))

menor = min(valores)
maior = max(valores)
indice_menor = valores.index(menor)
indice_maior = valores.index(maior)

print(f'Lista: {valores}')
print(f'O menor valor informado foi {min(valores)} no(s) indice(s): ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}... ', end='')

print()
print(f'O maior valor informado foi {max(valores)} no(s) indice(s): ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}... ', end='')
