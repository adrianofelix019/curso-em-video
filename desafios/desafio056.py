'''
Esse programa lê o nome, idade e sexo de 4 pessoas. No final mostra:
- A média de idade das pessoas
- O nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
'''

soma_das_idades = 0
nome_do_homem_mais_velho = ''
idade_do_homem_mais_velho = 0
mulheres_maiores_de_20 = 0

for c in range(0, 4):
    indice = c + 1

    print('----- {}ª PESSOA -----'.format(indice))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] : '))

    if sexo == 'm':
        if c == 0:
            nome_do_homem_mais_velho = nome
            idade_do_homem_mais_velho = idade

        if idade > idade_do_homem_mais_velho:
            nome_do_homem_mais_velho = nome
            idade_do_homem_mais_velho = idade

    if sexo == 'f':
        if idade > 20:
            mulheres_maiores_de_20 += 1

    soma_das_idades += idade

media_das_idades = soma_das_idades / 4
print('A média das idades informadas é {:.1f}'.format(media_das_idades))
print('O nome do homem mais velho é {}'.format(nome_do_homem_mais_velho))
print('A quantidade de mulheres com mais de 20 anos é {}'
      .format(mulheres_maiores_de_20))
