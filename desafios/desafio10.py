"""
Esse script lê um valor em reais e mostra esse valor convertido para dólares.
"""


real = float(input('Informe o valor em reais R$'))
dolar = real / 4.94
print('R${:.2f} convertido para dolar vale U${:.2f}'.format(real, dolar))
