valores = []
continuar = 's'

while continuar == 's':
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = input('Deseja continuar? [S/N]').lower().strip()[0]

valores.sort()
print(f'O valores informados foram {valores}')
