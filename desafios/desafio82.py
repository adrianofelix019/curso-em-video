numeros = []
impares = []
pares = []

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    continuar = str(input('Deseja continuar? (S/N) ')).strip().lower()

    if continuar == 'n':
        break

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Todos os números digitados foram: {numeros}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')