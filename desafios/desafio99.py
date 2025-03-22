from time import sleep


def linha():
    print('~'*50)


def maior(*numeros):
    print('Analisando os valores passados...')
    
    for numero in numeros:
        print(numero, end=' ', flush=True)
        sleep(0.5)
    
    print(f'Foram informados {len(numeros)} números ao todo.')
    sleep(1)
    if len(numeros) == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(numeros)}.')


linha()
maior(2, 9, 4, 5, 7, 1)
linha()
maior(4, 7, 0)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior()
