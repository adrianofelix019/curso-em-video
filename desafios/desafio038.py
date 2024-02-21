"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando
na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

if num1 > num2:
    print("O primeiro valor é maior")
elif num1 < num2:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")
