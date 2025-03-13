pessoas = []

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().lower()[0]

    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }

    pessoas.append(pessoa)

    continuar = input('Continuar? [S/N] ').lower().strip()[0]
    if continuar == 'n':
        break

print('-=' * 25)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')

soma_idade = 0
mulheres = []
for pessoa in pessoas:
    soma_idade += pessoa['idade']

    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa)
media_idade = soma_idade / len(pessoas)

print(f'A média de idade é {media_idade:.2f}')
print('As mulheres cadastradas foram: ')
for mulher in mulheres:
    print(f'\t{mulher['nome']}')

print('As pessoas com idade acima da média são:')
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        print(f'\t{pessoa['nome']}')
print('-='*25)
print('Finalizando...')