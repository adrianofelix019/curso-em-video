print('-=' * 16)
print('Gerador de progressão aritmetica')
print('-=' * 16)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ➝  '.format(termo), end='')
        cont += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos a mais deseja visualizar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
