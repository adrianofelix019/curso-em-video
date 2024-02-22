"""
Desenvolva um lógica que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

peso = float(input("Informe seu peso em Kg: "))
altura = float(input("Informe a sua altura em metros: "))
imc = peso / (altura**2)

print(f"Seu IMC é de {imc:.2f}")

if imc < 18.5:
    status = "Abaixo do peso"
elif imc <= 25:
    status = "Peso ideal"
elif imc < 30:
    status = "Sobrepeso"
elif imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade mórbida"

print(f"Seu status é: {status}")
