"""
Esse programa lê 3 números pelo teclado a mostra na tela o maior e o menor.
"""


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = n1
maior = n1

if n2 > maior and n2 > n3:
    maior = n2
elif n3 > maior:
    maior = n3

if n2 < menor and n2 < n3:
    menor = n2
elif n3 < menor:
    menor = n3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
