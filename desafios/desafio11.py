"""
Esse script lê a largura e altura de uma parede em metros, então calcula sua área
e a quantidade de tinta necessária para pintá-la, considerando que cada
litro de tinta pinta uma área de 2m².
"""


largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
print('Uma parede medindo {}mx{}m tem uma área de {}m².'.format(largura, altura, area))
tinta_necessaria = area / 2
print('Será necessário {:.2f}l de tinta para pintar essa parede.'.format(tinta_necessaria))
