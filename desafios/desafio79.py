numeros = []

while True:
  numero = int(input('Digite um valor: '))

  if numero not in numeros:
    numeros.append(numero)
    print('Valor adicionado com sucesso.')
  else:
    print('Valor duplicado, não vou adicionar.')

  resposta = str(input('Quer continuar? [S/N] ')).strip()[0]

  if resposta in 'Nn':
    break

print('-='*30)
numeros.sort()
print(f'Você digitou os números {numeros}.')
