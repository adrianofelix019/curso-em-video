from random import shuffle

"""
Esse script lê o nome de 4 alunos e sorteia a ordem de apresentação entre eles.
"""


aluno1 = input('Informe o nome do 1° aluno(a): ')
aluno2 = input('Informe o nome do 2° aluno(a): ')
aluno3 = input('Informe o nome do 3° aluno(a): ')
aluno4 = input('Informe o nome do 4° aluno(a): ')
equipe = [aluno1, aluno2, aluno3, aluno4]
shuffle(equipe)
print('A ordem de apresentação será {}.'.format(equipe))
