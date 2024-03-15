from math import hypot

"""
Esse script lê pelo teclado o cateto aposto e adjacente de um triângulo 
retângulo e então calcula e mostra o comprimento da hipotenusa.
"""

cateto_oposto = float(input('Informa o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('O comprimento da hipotenusa desse triângulo vale {:.2f}.'.format(hipotenusa))
