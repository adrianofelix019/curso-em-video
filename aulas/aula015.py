soma = 0

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break

    soma += num

# print('A soma dos valores digitados é igual a {}'.format(soma))
print(f'A soma dos valores digitados é igual a {soma}.')
