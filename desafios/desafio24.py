"""
Esse programa lê o nome de uma cidade pelo teclado e verifica se ele começa
com Santo.
"""

nome = input('Informe o nome da cidade: ').strip().lower()
print('A cidade começa com Santo? ', end='')
print(nome.startswith('santo'))
