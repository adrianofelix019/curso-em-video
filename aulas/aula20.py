def soma(*valores):
    s = 0
    for valor in valores:
        s += valor
    print(f'Somando {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
