alunos = []
dados = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    continuar = str(input('Continuar? [S/N] ')).strip().lower()[0]

    if continuar == 'n':
        break

print('-='*25)
print(f'{"N°":<3}{"Nome":<15}{"Média":<15}')
print('-'*33)
for indice, aluno in enumerate(alunos):
    print(f'{indice:<3}{aluno[0]:<15}{aluno[2]:<15.1f}')

while True:
    indice = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if indice == 999:
        break
    if indice <= len(alunos) - 1:
        print(f'As notas de {alunos[indice][0]} são {alunos[indice][1]}')
    print('-' * 50)

print('<' * 3, 'Volte sempre!', '>' * 3)
