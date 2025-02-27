numeros = [[], []]

for c in range(7):
    pares = numeros[0]
    impares = numeros[1]
    numero = int(input(f'Informe o {c+1}° número: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('-='*30)
numeros[0].sort()
numeros[1].sort()
print(f'Valores pares: {numeros[0]}')
print(f'Valores ímpares: {numeros[1]}')
