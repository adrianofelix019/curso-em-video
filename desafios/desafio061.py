primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

contador = primeiro
while contador <= decimo:
    print(contador, end=' ➝  ')
    contador += razao
print('FIM')
