brasileirão = (
    'Botafogo',
    'Palmeiras',
    'Flamengo',
    'Fortaleza',
    'São Paulo',
    'Bahia',
    'Cruzeiro',
    'Athletico-PR',
    'Bragantino',
    'Atlético-MG',
    'Vasco da Gama',
    'Juventude',
    'Internacional',
    'Corinthians',
    'Criciúma',
    'Cuiabá',
    'EC Vitória',
    'Grêmio',
    'Fluminense',
    'Atlético-GO'
)

print(f'Ao todo temos {len(brasileirão)} times competindo no Brasileirão.')
for indice, time in enumerate(brasileirão):
    colocação = str(indice + 1) + '°'
    print(f'{colocação:<3} - {time}')

print('-='*25)

print('Os 5 primeiros colocados do Brasileirão são:')
for indice, time in enumerate(brasileirão[:5]):
    colocação = str(indice + 1) + '°'
    print(f'{colocação:<2} - {time}')

print('-='*25)

print('Os 4 últimos colocados são:')
for indice, time in enumerate(brasileirão[-4:]):
    colocação = str(len(brasileirão) - (4 - (indice + 1))) + '°'
    print(f'{colocação:<2} - {time}')

print('-='*25)

print('Os times do Brasileirão em ordem alfabética:')
for time in sorted(brasileirão):
    print(time)

print('-='*25)
print(f'O Vasco da Gama está na {brasileirão.index('Vasco da Gama')+1}ª posição.')
