n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))
n3 = int(input('Digite o valor 3: '))
n4 = int(input('Digite o valor 4: '))

nums = (n1, n2, n3, n4)
print(f'Você digitou os valores: {nums}')
print(f'O número 9 apareceu {nums.count(9)} vezes.')

if nums.count(3) != 0:
    print(f'O valor 3 está na posição {nums.index(3) + 1}')
else:
    print(f'O valor 3 não foi digitado.')

print('Os números pares digitados foram ', end='')
for num in nums:
    if num % 2 == 0:
        print(num, end=' ')
