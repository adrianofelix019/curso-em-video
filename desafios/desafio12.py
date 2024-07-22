"""
Esse script lê o preço de um produto e mostra seu novo preço com 5% de desconto.
"""


preço = float(input('Informe o preço do produto: '))
preço_com_desconto = preço * 0.95 
print('R${:.2f} com 5% desconto será R${:.2f}'.format(preço, preço_com_desconto))
