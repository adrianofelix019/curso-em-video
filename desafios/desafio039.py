from datetime import date
"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo
com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

ano_de_nascimento = int(input("Ano de nascimento "))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
tempo_alistamento = idade - 18
print(f"Quem nasceu em {ano_de_nascimento} tem {idade} anos.")
if idade < 18:
    print("Ainda não chegou a hora de se alistar.")
    print(f"Faltam {abs(tempo_alistamento)} anos.")
    print(f"Seu alistamento será no ano de {ano_de_nascimento + 18}.")
elif idade == 18:
    print("Chegou a hora de se alistar.")
else:
    print("Já passou o tempo de se alistar.")
    print(f"Já passaram {tempo_alistamento} anos.")
    print(f"Seu alistamento deveria ter sido no ano de {ano_de_nascimento + 18}.")
