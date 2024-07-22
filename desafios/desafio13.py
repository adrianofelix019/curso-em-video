"""
Esse script lê o salário de um funcionario e mostra seu novo salario com 15% de
aumento.
"""


salario_atual = float(input('Informe o salário atual: '))
novo_salario = salario_atual * 1.15
print('R${:.2f} com 15% de aumento será R${:.2f}.'.format(salario_atual, novo_salario))
