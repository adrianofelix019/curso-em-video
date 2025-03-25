def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano_nascimento
    resultado = ''

    if idade < 16:
        resultado = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        resultado = 'VOTO OPCIONAL'
    else:
        resultado = 'VOTO OBRIGATÓRIO'
    
    return f'Com {idade} anos: {resultado}'


print('-=' * 25)
ano_nascimento = int(input('Em que você nasceu? '))
print(voto(ano_nascimento))