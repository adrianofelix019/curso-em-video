from random import randint
from time import sleep


def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    for i in range(5):
        numero = randint(1, 10)
        sleep(1)
        print(f'{numero} ', end='', flush=True)
        numeros.append(numero)
    print('Pronto!')


def soma_par(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


numeros = []
sorteia(numeros)
soma_par(numeros)
