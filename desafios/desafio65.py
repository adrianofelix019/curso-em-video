maior = menor = float(input('Digite algum valor: '))
soma = maior
total = 1
continuar = input('Deseja continuar? (S/N): ').strip().lower()

while continuar != 'n':

    n = float(input('Digite algum valor: '))

    soma += n
    total += 1

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    continuar = input('Deseja continuar? (S/N): ').strip().lower()

media = soma / total
print('Você digitou {} números.'.format(total))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
print('E a média entre os valores digitados é igual a {:.2f}'.format(media))
