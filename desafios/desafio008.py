"""
Esse script lê um valor em metros e mostra na tela a conversão para centimetros
e milimetros.
"""


metros = float(input('Informe um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print('{}m convertido para centimetros vale {}cm.'.format(metros, centimetros))
print('{}m convertido para milimetros vale {}mm'.format(metros, milimetros))
