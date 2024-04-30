numero = 0
soma = 0
total = 0
while numero != 999:
    numero = float(input('Informe algum valor para somar (999 para sair): '))
    if numero != 999:
        soma += numero
        total += 1

print('-='*18)
print('Ao todo foram informados {} valores.'.format(total))
print('E a soma entre eles é igual a {}'.format(soma))
print('-='*18)
