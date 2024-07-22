'''
Esse programa lê o peso de 5 pessoas e depois mostra na tela o menor a o maior
peso lidos.
'''

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Informe o peso {}:'.format(c + 1)))

    if c == 0:
        menor = peso
        maior = peso

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print('O maior peso lido foi {:.2f}Kg'.format(maior))
print('O menor peso lifo foi {:.2f}Kg'.format(menor))
