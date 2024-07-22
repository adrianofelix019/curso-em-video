'''
Esse programa lê 6 números inteiros e mostra a soma apenas dos valores pares.
Se o valor digitado for ímpar ela será desconsiderado.
'''

soma = 0
contador = 0
for c in range(0, 6):
    n = int(input('Digite o {}º valor: '.format(c+1)))

    if n % 2 == 0:
        soma += n
        contador += 1

print('Você informou {} números \033[1mpares\033[0m e a soma é igual a {}'
      .format(contador, soma))
