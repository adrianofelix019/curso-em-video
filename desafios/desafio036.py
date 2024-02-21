"""
Escreva um programa para aprovar o emprestimo bancario para compra de uma casa
O programa vai perguntar o valor da casa, o salario do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
salario ou então o emprestimo será negado
"""

valor_da_casa = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o seu salário? "))
anos_de_financiamento = int(input("Em quantos anos deseja pagar? "))
valor_prestação = (valor_da_casa / (anos_de_financiamento * 12))

print(f"O valor da prestação será {valor_prestação:.2f}")
if valor_prestação > (salario * 0.3):
    print("Infelizmente seu financiamento não foi aprovado.")
else:
    print("Parabéns! Seu financiamento foi aprovado!")
