n = 1
pares = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares += 1
print('Ao todo foram informados {} número pares'.format(pares))
