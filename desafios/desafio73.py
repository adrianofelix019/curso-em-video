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
print('Os 5 primeiros colocados do Brasileirão são:')
for time in brasileirão[:5]:
    print(time)

print('Os 4 últimos colocados são:')
for i in range(len(brasileirão) - 4, len(brasileirão)):
    brasileirão[i]

print('-='*25)
print('Os times do Brasileirão em ordem alfabética:')
for time in sorted(brasileirão):
    print(time)

# TODO: Em que posição da tabela está o time da Chapecoense.
print('-='*25)
print(f'O Vasco da Gama está na {brasileirão.index('Vasco da Gama')}ª posição.')
