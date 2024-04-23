import datetime

'''
Esse programa lê a data de nascimento de 7 pessoas e então mostra quantas ainda
não atingiram a maior idade e quantas já são de maior.
'''

menores = 0
maiores = 0
ano_atual = datetime.date.today().year
for c in range(0, 7):
    ano_nascimento = int(input('Informe a data de nascimento {}: '
                               .format(c+1)))
    if ano_atual - ano_nascimento < 18:
        menores += 1
    else:
        maiores += 1
print('Ao todo foram {} menores de idade.'.format(menores))
print('E {} maiores de idade.'.format(maiores))
