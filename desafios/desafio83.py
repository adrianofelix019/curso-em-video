expressão = input('Digite a expressão: ')
pilha = []

for char in expressão:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

print('-='*30)
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
