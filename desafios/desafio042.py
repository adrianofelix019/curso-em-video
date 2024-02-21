"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
print("Informe os 3 lados do triângulo")
lado1 = int(input("Primeiro lado: "))
lado2 = int(input("Segundo lado: "))
lado3 = int(input("Terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print(f"É possível formar um triângulo com ({lado1}, {lado2}, {lado3})")
else:
    print(f"Não é possível formar um triângulo com ({lado1}, {lado2}, {lado3})")

if lado1 == lado2 and lado2 == lado3:
    tipo_de_triangulo = "equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo_de_triangulo = "isósceles"
else:
    tipo_de_triangulo = "escaleno"

print(f"O triângulo formado será {tipo_de_triangulo}.")
