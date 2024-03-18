"""
Programa para exibir o primeiro e última nome.
"""


nome = input('Informe seu nome: ')
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]
print('Seu primeiro nome é {}'.format(primeiro_nome))
print('Seu último nome é {}'.format(ultimo_nome))
