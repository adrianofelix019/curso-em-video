from datetime import date

"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria de acordo com sua idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

ano = int(input("Ano do nascimento: "))
idade = date.today().year - ano

print(f"Você tem {idade} anos de idade.")
if idade <= 9:
    print("Sua categoria é mirim.")
elif idade <= 14:
    print("Sua categoria é infantil.")
elif idade <= 19:
    print("Sua categoria é junior.")
elif idade <= 20:
    print("Sua categoria é sênior.")
else:
    print("Sua categoria é master.")
