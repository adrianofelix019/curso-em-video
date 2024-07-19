maiores_de_idade = 0
homens = 0
mulheres_com_menos_de_20_anos = 0

while True:
    print('-'*60)
    print(f'{"CADASTRE UMA PESSOA":^60}')
    print('-'*60)
    idade = int(input('Informe sua idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo (M/F): ')).strip().upper()[0]

    if idade > 18:
        maiores_de_idade += 1

    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff' and idade < 20:
        mulheres_com_menos_de_20_anos += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).strip().upper()[0]

    if continuar in 'Nn':
        print('Saindo...')
        break

print(f'Ao todo foram cadastrados {maiores_de_idade} maiores de idade.')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {mulheres_com_menos_de_20_anos}')
