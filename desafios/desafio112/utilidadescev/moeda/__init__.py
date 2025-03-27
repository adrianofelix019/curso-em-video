def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, aumento=0, formatado=False):
    aumento /= 100
    resultado = valor * (1 + aumento)
    if formatado:
        return moeda(resultado)
    else:
        return resultado


def diminuir(valor=0, desconto=0, formatado=False):
    desconto /= 100
    resultado = valor * (1 - desconto)
    if formatado:
        return moeda(resultado)
    else:
        return resultado


def dobro(valor=0, formatado=False):
    if formatado:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor=0, formatado=False):
    if formatado:
        return moeda(valor / 2)
    else:
        return valor / 2


def resumo(valor=0, taxa=5, desconto=10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: {moeda(valor)}')
    print(f'O dobro de {moeda(valor)}:\t{dobro(valor, True)}.')
    print(f'Metade de {moeda(valor)}:\t{metade(valor, True)}.')
    print(f'Com taxa de {taxa}%:\t{aumentar(valor, taxa, True)}.')
    print(f'Com desconto de {desconto}%:\t{diminuir(valor, desconto, True)}.')
    print('-' * 30)
