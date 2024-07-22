"""
Faça um programa que mostre na tela uma contagem regressiva para os estouros de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep

print('CONTAGEM REGRESSIVA PARA O ANO NOVO!')
for segundo in range(10, 0, -1):
    print(f'{segundo}!')
    sleep(1)
print('FELIZ ANO NOVO! 🥳')
