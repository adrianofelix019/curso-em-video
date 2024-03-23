import datetime

"""
Programa para verificar se um ano é bissexto.
"""


print('Digite 0 para verificar o ano atual.')
ano = int(input('Informe o ano para verificar se é bissexto: '))

if ano == 0:
    ano = datetime.datetime.today().year

if ano % 4 == 0 and ano % 100 != 0:
    print(f'{ano} é bissexto.')
elif ano % 400 == 0:
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto.')
