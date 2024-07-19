print('='*50)
print(f'{'BANCO CEV':^50}')
print('='*50)

valor = int(input('Quanto quer sacar? R$'))
total = valor
cedula_atual = 50
total_de_cedula = 0

while True:
    if total >= cedula_atual:
        total -= cedula_atual
        total_de_cedula += 1
    else:
        if total_de_cedula > 0:
            print(f'Total de {total_de_cedula} cedulas de R${cedula_atual}')

        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_de_cedula = 0

        if total == 0:
            break
