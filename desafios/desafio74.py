from random import randint

n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)
num_aleatorios = (n1, n2, n3, n4, n5)
print(f'Os números aleatórios gerados foram: {num_aleatorios}')
print(f'Maior valor: {max(num_aleatorios)}')
print(f'Menor valor: {min(num_aleatorios)}')
