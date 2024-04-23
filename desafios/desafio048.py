"""
Esse script mostra na tela a soma de todos os números ímpares que são multiplos
de 3 e se encontram no intervalo entre 1 e 500
"""
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c

print("A soma de todos os {} números ímpares e multiplos de 3 entre 1 e 500"
      .format(contador))
print("É igual a {}".format(soma))
