"""
Programa lê o nome de uma pessoa pelo teclado e mostra na tela se tem Silva no
nome.
"""


nome = input('Escreva seu nome: ').strip()
print('Você tem Silva no nome? ', end='')
print('silva' in nome.lower())
