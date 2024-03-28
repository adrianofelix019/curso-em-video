"""
Programa que calcula o valor a ser pago por um produto considerando
seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

preço = float(input("Informe o preço do produto: "))
metodo_de_pagamento = int(input("""
Informe o método de pagamento
[1] - À vista dinheiro/cheque
[2] - À vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão
"""))

if metodo_de_pagamento == 1:
    preço_final = preço * 0.9
elif metodo_de_pagamento == 2:
    preço_final = preço * 0.95
elif metodo_de_pagamento == 3:
    preço_final = preço
    parcela = preço_final / 2
    print(f'Sua compra de R${preço_final:.2f} será dividida em 2x de {parcela:.2f} sem juros!')
elif metodo_de_pagamento == 4:
    preço_final = preço * 1.2
    parcelas = int(input('Em quantas vezes deseja pagar? '))
    parcela = preço_final / parcelas
    print(f'Sua compra será dividida em {parcelas}x de {parcela:.2f} com juros.')
else:
    preço_final = preço
    print('Opção de pagamento inválida, tente novamente.')

print(f'Sua compra de R${preço:.2f} vai custar R${preço_final:.2f} no final')
