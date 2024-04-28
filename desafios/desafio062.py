primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + 10 * razao

contador = primeiro
while contador <= decimo:
    print(contador, end=' -> ')
    contador += razao

    if contador == decimo:
        continuar = int(
            input('Quer visualizar mais termos? (Digite 0 para sair) ')
        )
        print()
        if continuar != 0:
            contador = decimo
            decimo = decimo + (continuar) * razao
        else:
            print('Saindo...')

print('FIM')
