"""
Esse programa lê pelo teclado o nome completo de uma pessoa e mostra na tela:

- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras tem ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""

nome = input('Informe seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('O seu nome tem {} letras ao todo.'.format(len(nome.replace(' ', ''))))
print('O seu primeiro nome tem {} letras.'.format(len(nome.split()[0])))
