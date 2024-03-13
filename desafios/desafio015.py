"""
Esse programa pergunta a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcula o preço a
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""


d = int(input('Quantos dias alugado? '))
kr = float(input('Quantos Km rodados? '))
total = (d * 60) + (kr * 0.15)
print('O total a pagar é R${:.2f}'.format(total))
