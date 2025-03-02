alunos = []
dados = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    alunos.append(dados[:])
    dados.clear()

    continuar = str(input('Continuar? [S/N] ')).strip().lower()[0]

    if continuar == 'n':
        break

print('-='*25)
print(f'{"N°":<3}{"Nome":<15}{"Média":<15}')
print('-'*33)
for indice, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{indice+1:<3}{aluno[0]:<15}{media:<15}')

while True:
    indice = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if indice == 999:
        break
    print(f'As notas de {alunos[indice][0]} são [{alunos[indice][1]}, {alunos[indice][2]}]')
