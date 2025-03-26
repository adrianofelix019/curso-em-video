def aumentar(valor, aumento):
    aumento /= 100
    return valor * (1 + aumento)


def diminuir(valor, desconto):
    desconto /= 100
    return valor * (1 - desconto)


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2
