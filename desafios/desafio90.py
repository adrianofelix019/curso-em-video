nome = input('Nome: ')
média = float(input(f'Média de {nome}: '))
situação = 'aprovado' if média >= 7 else 'reprovado'
aluno = { 'nome': nome, 'média': média,  'situação': situação }

print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['média']}')
print(f'Situação é igual a {aluno["situação"]}')
