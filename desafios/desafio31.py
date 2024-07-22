"""
Programa para calcular o valor de uma viagem com base na distância.
- Serão cobrados R$0,50 por Km para viagens de até 200Km
- Para viagens mais longas será cobrado R$0,45 por Km
"""


distancia = int(input('Informe a distancia da viagem: '))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print('Para uma viagem de {}Km'.format(distancia))
print('O valor da passagem será R${:.2f}'.format(valor))
