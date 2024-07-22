numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = -1
while numero not in range(0, 20):
    numero = int(input('Digite um número 0 e 20: '))
print(f'Você digitou o número {numeros[numero]}.')
