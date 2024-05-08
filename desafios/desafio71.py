print('='*50)
print(f'{'BANCO CEV':^50}')
print('='*50)
valor = int(input('Quanto quer sacar? R$'))

cinquenta = valor // 50
vinte = valor % 50 // 20
dez = valor % 50 % 20 // 10
um = valor % 50 % 20 % 10 // 1

print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas notas de R$20')
print(f'Total de {dez} cédulas notas de R$10')
print(f'Total de {um} cédulas notas de R$1')
print('='*50)
print('Volte sempre ao banco CEV! Tenha um bom dia!')
