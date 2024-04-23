'''
Esse programa lê o primeiro termo e a razão de uma progressão aritmetica e
mostra na tela os 10 primeiros termos dessa progressão.
'''

primeiro_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo + 1, razao):
    print(c, end=' ➝  ')

print('FIM')
