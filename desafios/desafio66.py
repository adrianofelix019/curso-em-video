soma = 0
total = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))

    if num == 999:
        break

    soma += num
    total += 1

print(f'A soma do(s) {total} valores foi {soma}!')
