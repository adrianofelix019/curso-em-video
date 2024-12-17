numeros = []
continuar = ''

while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? (S/N) ').strip()[0]

    if continuar in 'Nn':
        break

print(f'{'-='*30} Algumas Informações {'-='*30}')
print(f'Os valores informados foram: {numeros}')
print(f'Ao todo foram informados {len(numeros)} valores')
lista_original = numeros[:]
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente: {numeros}')

if 5 in numeros:
    print(f'O valor 5 foi digitado {numeros.count(5)} vez(es)')
    print('Nos indices: ', end='')
    for indice, numero in enumerate(lista_original):
        if numero == 5:
            print(f'{indice} ', end='')
else:
    print('O número 5 não foi digitado nenhuma vez.')
