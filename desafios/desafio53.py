'''
Esse programa lê uma frase qualquer pelo teclado e informa se ela é um
palindromo.
'''

frase = str(input('Digite algo: ')).upper()
frase_reversa = frase[::-1].replace(' ', '').upper()

print('O inverso de {} é {}'.format(frase, frase_reversa))
if frase_reversa == frase.replace(' ', ''):
    print('{} é um palindromo.'.format(frase))
else:
    print('{} não é um palindromo.'.format(frase))
