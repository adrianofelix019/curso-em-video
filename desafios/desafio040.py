"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida.

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média superior a 7.0: APROVADO
"""

nota1 = float(input("Informe a primeiora nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A média foi {media:.2f}")
if media < 5:
    print("REPROVADO")
elif media < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
