vermelho = '\033[31m'
limpar = '\033[0m'


def leiaDinheiro(mensagem):
    valido = False
    
    while not valido:
        valor = input(mensagem).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'{vermelho}ERRO! "{valor}" não é um preço válido.{limpar}')
        else:
            valido = True
    
    return float(valor)
