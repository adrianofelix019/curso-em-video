'''
Esse programa lê 6 números inteiros e mostra a soma apenas dos valores pares.
Se o valor digitado for ímpar ela será desconsiderado.
'''

soma = 0
for c in range(0, 6):
    n = int(input('Digite o {}º valor: '.format(c+1)))

    if n % 2 == 0:
        soma += n
print('A soma de todos os valores pares é igual a {}'.format(soma))
