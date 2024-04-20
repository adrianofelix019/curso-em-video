'''
Esse programa lê uma frase qualquer pelo teclado e informa se ela é um
palindromo.
'''

frase = str(input('Digite algo: '))
frase_reversa = frase[::-1].replace(' ', '')

if frase_reversa == frase.replace(' ', ''):
    print('{} é um palindromo.'.format(frase))
else:
    print('{} não é um palindromo.'.format(frase))
