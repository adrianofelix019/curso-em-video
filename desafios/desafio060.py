num = int(input('Informe um número inteiro para calcular seu fatorial: '))
resultado = 1
c = num

while c > 1:
    resultado *= c
    c -= 1

print('{}! é igual a {}'.format(num, resultado))
