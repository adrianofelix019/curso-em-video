n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

smallest = n1
higher = n1

if n2 > higher and n2 > n3:
    higher = n2
elif n3 > higher:
    higher = n3

if n2 < smallest and n2 < n3:
    smallest = n2
elif n3 < smallest:
    smallest = n3

print(f'The higher number is {higher}')
print(f'The smallest number is {smallest}')