'''
Esse programa lê um sexo de uma pessoa mas só aceita os valores 'M' ou 'F'
caso um valor incorreto seja inserido terá que digitar novamente.
'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo: [F/M] ').upper()

print(f'Seu sexo é {sexo}')
