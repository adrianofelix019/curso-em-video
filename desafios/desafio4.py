"""
Esse script lê um valor e mostra seu tipo e todas as informações possíveis sobre
ele.
"""


valor = input('Digite algo: ')
print('Você digitou {}'.format(valor))
print('Tipo: {}'.format(type(valor)))
print('É apenas espaços em branco? {}'.format(valor.isspace()))
print('É númerico? {}'.format(valor.isnumeric()))
print('É alfabetico? {}'.format(valor.isalpha()))
print('É alfa-númerico? {}'.format(valor.isalnum()))
print('Está em maiusculas? {}'.format(valor.isupper()))
print('Está em minusculas? {}'.format(valor.islower()))
print('É um título? {}'.format(valor.istitle()))
