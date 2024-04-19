'''
Esse script lê um número pelo teclado e mostra na tela sua tabuada.
Diferente do desafio 009, aqui será usado a estrutura de repetição for
'''

n = int(input('Informe um número para ver sua tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, (n * c)))
