from datetime import datetime


def voto(idade):
    resultado = ''

    if idade < 16 or idade >= 60:
        resultado = 'VOTO OPCIONAL'
    else:
        resultado = 'VOTO OBRIGATORIO'
    
    return resultado


print('-=' * 25)
ano_nascimento = int(input('Em que você nasceu? '))
idade = datetime.now().year - ano_nascimento
print(f'Com {idade} anos: {voto(idade)}')
