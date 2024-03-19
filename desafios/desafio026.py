"""
Esse programa lê uma frase pelo teclado e mostra na tela:

- Quantas vezes aparece a letra A
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez
"""


frase = input('Digite qualquer coisa: ').strip()
print('A letra A aparece {} vezes.'.format(frase.lower().count('a')))
primeira_ocorrencia = frase.lower().find('a') + 1
ultima_ocorrencia = frase.lower().rfind('a') + 1
print('Ela aparece pela primeira vez no índice {}'.format(primeira_ocorrencia))
print('Ela aparece pela últma vez no índice {}'.format(ultima_ocorrencia))
