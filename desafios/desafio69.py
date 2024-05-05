maiores_de_idade = 0
homens = 0
mulheres_com_menos_de_20_anos = 0

while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo (M/F): '))
    continuar = str(input('Quer continuar? (S/N) ')).strip()

    if idade > 18:
        maiores_de_idade += 1

    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff' and idade < 20:
        mulheres_com_menos_de_20_anos += 1

    if continuar in 'Nn':
        print('Saindo...')
        break

print(f'Ao todo foram cadastrados {maiores_de_idade} maiores de idade.')
print(f'E {homens} homens foram cadastrados.')
print(f'E também {mulheres_com_menos_de_20_anos}', end='')
print('Mulheres com menos de 20 anos foram cadastradas.')
