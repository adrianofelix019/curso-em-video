"""
Esse script faz uma contagem regressiva de 10 até 0 e mostra uma mensagem de
feliz ano novo.
"""

from time import sleep

for c in range(10, 0, -1):
    print("{}!".format(c))
    sleep(1)
print("Feliz ano novo! 🥳🎉🎊")
