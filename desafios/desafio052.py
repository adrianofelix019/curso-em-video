'''
Esse programa lê um número inteiro e mostra na tela se ele é ou não um número
primo.
'''

n = int(input('Informe um número para verificar se ele é primo: '))

e_primo = True
for c in range(2, n):
    if n % c == 0:
        e_primo = False
print('O número {} é primo? {}'.format(n, e_primo))
