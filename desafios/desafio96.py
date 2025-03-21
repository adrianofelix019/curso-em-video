def calcular_area(largura, comprimento):
    area = largura * comprimento
    print(f'A Área de um terro {largura:.1f}x{comprimento:.1f} é igual a {area:.1f}m².')


print('Controle de Terrenos')
print('--------------------')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calcular_area(largura, comprimento)
