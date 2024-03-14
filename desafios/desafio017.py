from math import pow, sqrt

"""
Esse script lê pelo teclado o cateto aposto e adjacente de um triângulo 
retângulo e então calcula e mostra o comprimento da hipotenusa.
"""


cateto_oposto = float(input('Informa o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
print('O comprimento da hipotenusa desse triângulo vale {}.'.format(hipotenusa))