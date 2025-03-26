def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentar(valor=0, aumento=0):
    aumento /= 100
    resultado = valor * (1 + aumento)
    return moeda(resultado)


def diminuir(valor=0, desconto=0):
    desconto /= 100
    resultado = valor * (1 - desconto)
    return moeda(resultado)


def dobro(valor=0):
    return moeda(valor * 2)


def metade(valor=0):
    return moeda(valor / 2)
