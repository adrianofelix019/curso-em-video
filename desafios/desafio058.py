from random import randint

print('Vou pensar num número entre 1 e 10, tente advinhar.')
secreto = randint(1, 10)
tentativas = 0
acertou = False

while not acertou:
    num = int(input('Qual seu palpite: '))
    tentativas += 1

    if secreto == num:
        acertou = True
    else:
        if secreto > num:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez.')

print('Você acertou, eu pensei no número {}'.format(secreto))
print('Você precisou de {} tentativas.'.format(tentativas))
