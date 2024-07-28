numeros_por_extenso = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
    'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
    'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 
    'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

continuar = 's'

while continuar in 'Ss':
    numero = -1
    while numero not in range(0, 21):
        numero = int(input('Digite um número 0 e 20: '))
    print(f'Você digitou o número {numeros_por_extenso[numero]}.')

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? (S/N): ').strip()[0]
print('Saindo...')
