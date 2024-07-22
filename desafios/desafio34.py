"""
Programa para calcular o aumento de salário de um funcionário.
- Salários de até 1250 recebem aumento de 15%
- Salários maiores que 1250 recebem aumento de 10%
"""


salario = float(input('Digite o salário: '))
aumento = 0

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print('O aumenta será de R${:.2f}'.format(aumento))
print('O novo salário será de R${:.2f}'.format(salario + aumento))
