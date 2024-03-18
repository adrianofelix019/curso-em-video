"""
Esse programa lê uma frase pelo teclado e mostra na tela:

- Quantas vezes aparece a letra A
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez
"""


frase = input('Digite qualquer coisa: ')
print('A letra A aparece {} vezes.'.format(frase.lower().count('a')))
print('Ela aparece pela primeira vez no índice {}'.format(frase.lower().find('a')))
print('Ela aparece pela últma vez no índice {}'.format(frase.lower().rfind('a')))
