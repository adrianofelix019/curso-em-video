"""
Programa para calcular multa de velocidade.

A velicidade é lida pelo teclado.

Regras:
- Se ultrapassar 80Km/h será exibida uma mensagem de multa.
- A multa vai custar R$7,00 para cada Km acima do limite.
"""


velocidade = int(input('Informe a velocidade do veículo: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Sua multa será de R${:.2f}'.format(multa))
else:
    print('Continue sua viagem em segurança.')
