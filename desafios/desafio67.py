while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))

    if valor < 0:
        break

    print('-=' * 6)
    for n in range(1, 11):
        print(f'{valor:2} x {n:2} = {valor * n:2}')
    print('-=' * 6)
