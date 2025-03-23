def par(num):
    return num % 2 == 0


n = int(input('Digite um número: '))
print(f'{n} é um número {'par' if par(n) else 'impar'}')
