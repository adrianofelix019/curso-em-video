from time import sleep


def contador(inicio, fim, passo):
    acrescimo = 0

    if passo == 0:
        passo = 1

    if inicio > fim:
        passo = -abs(passo)
        acrescimo = -1
    else:
        passo = abs(passo)
        acrescimo = 1

    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}.')

    for c in range(inicio, fim + acrescimo, passo):
        print(f'{c} ', end='', flush=True)
        sleep(.5)

    print('Fim!')


print('~'*25)
contador(1, 10, 1)
print('~'*25)
contador(10, 0, 2)
print('~'*25)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('~'*25)
contador(inicio, fim, passo)
