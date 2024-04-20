'''
Esse programa lê o primeiro termo e a razão de uma progressão aritmetica e
mostra na tela os 10 primeiros termos dessa progressão.
'''

primeiro_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
proximo_termo = primeiro_termo
for c in range(0, 10):
    print(proximo_termo, end=', ')
    proximo_termo += razao
