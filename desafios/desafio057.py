'''
Esse programa lê um sexo de uma pessoa mas só aceita os valores 'M' ou 'F'
caso um valor incorreto seja inserido terá que digitar novamente.
'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(
        input('Dados inválidos, por favor informe seu sexo: ')
    ).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
