from random import choice

"""
Script para sortear um nome entre quatro alunos.
"""


aluno1 = input('Informe o nome do 1° aluno(a): ')
aluno2 = input('Informe o nome do 2° aluno(a): ')
aluno3 = input('Informe o nome do 3° aluno(a): ')
aluno4 = input('Informe o nome do 4° aluno(a): ')
# aluno_sorteado = random.randint(1, 4)
alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = choice(alunos)
print('O aluno(a) sorteado foi {}.'.format(aluno_sorteado))
