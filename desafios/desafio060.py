num = int(input('Informe um número inteiro para calcular seu fatorial: '))
contador = num
fatorial = 1

while contador > 0:
    print(contador, end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1

print(fatorial)
