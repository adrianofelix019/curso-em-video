"""
Esse programa lê um número inteiro qualquer e pede ao usuário para escolher
qual será a base de conversão:
1 - para binário
2 - para octal
3 - hexadecimal
"""

num = int(input("Informe um número: "))
base = int(input("""Para que base deseja converter o número?
1 - Binário
2 - Octal
3 - Hexadecimal
Opção: """))

if base == 1:
    num_convertido = bin(num)
elif base == 2:
    num_convertido = oct(num)
elif base == 3:
    num_convertido = hex(num)


# fatiamento para remover o prefixo da base
print(f"O número {num} convertido é {num_convertido[2:]}")
