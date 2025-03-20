pessoas = []

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))

    while True:
        sexo = input('Sexo [M/F]: ').strip().lower()[0]
        if sexo in 'mf':
            break
        else:
            print('Por favor digite apenas M ou F.')

    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }

    pessoas.append(pessoa)

    while True:
        continuar = input('Continuar? [S/N] ').lower().strip()[0]
        if continuar in 'sn':
            break
        else:
            print('Por favor responda apenas S ou N.')

    if continuar == 'n':
        break

print('-=' * 25)

soma_idade = 0
mulheres = []
for pessoa in pessoas:
    soma_idade += pessoa['idade']

    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa)

media_idade = soma_idade / len(pessoas)

print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é {media_idade:.1f}')
print('C) As mulheres cadastradas foram: ')
for mulher in mulheres:
    print(f'\t{mulher['nome']}')

print('D) As pessoas com idade acima da média são:')
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        print(f'\t{pessoa['nome']} com {pessoa['idade']} anos de idade.')
print('-='*25)
print('Finalizando...')
