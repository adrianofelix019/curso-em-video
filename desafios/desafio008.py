"""
Esse script lê um valor em metros e mostra na tela a conversão para centimetros
e milimetros.
"""


medida = float(input('Informe um valor em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print('{}m convertido para centimetros vale {:.0f}cm.'.format(medida, centimetros))
print('{}m convertido para milimetros vale {:.0f}mm'.format(medida, milimetros))
