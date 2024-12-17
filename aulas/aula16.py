num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2) # remove a primeira ocorrencia

if 4 in num:
    num.remove(4) # remover um elemento que não está na lista gera uma excessão
else:
    print('4 não está na lista.')

print(num)
print(f'Essa lista tem {len(num)} elementos.')

print('-'*100)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

valores = []
# for c in range(5):
#     valores.append(int(input(f'Digite o {c+1}° valor: ')))

for chave, valor in enumerate(valores):
    print(f'{chave}: {valor}')
print('Cheguei ao final da lista.')

print('-'*100)

a = [1, 2, 3, 4, 5]
b = a[:]

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
