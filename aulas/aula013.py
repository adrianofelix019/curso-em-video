soma = 0

for c in range(0, 3):
    numero = int(input('Informe um valor: '))
    soma += numero
print(f'O somatório de todos os valores foi {soma}')


def average(values: list[float]) -> float:
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)


print(average([9.5, 10.0]))
