"""
Esse programa lê os três lados de um possível triângulo e informa na tela se é
possível formar-lo com os dados fornecidos.
"""


l1 = int(input('Informe o primeiro lado: '))
l2 = int(input('Informe o segundo lado: '))
l3 = int(input('Informe o terceiro lado: '))

condicao1 = (l2 - l3) < l1 < l2 + l3
condicao2 = (l3 - l1) < l2 < l3 + l1
condicao3 = (l1 - l2) < l3 < l1 + l2

if condicao1 and condicao2 and condicao3:
    print(f"{l1}, {l2} e {l3} podem formar um triângulo.")
else:
    print(f"{l1}, {l2} e {l3} não podem formar um triângulo.")
