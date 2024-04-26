from random import randint

secreto = randint(1, 10)
num = int(input('Vou pensar num número entre 1 e 0, tente advinhar: '))
tentativas = 1

while secreto != num:
    num = int(input('Você errou, tente mais uma vez: '))
    tentativas += 1

print('Você acertou, eu pensei no número {}'.format(secreto))
print('Você precisou de {} tentativas.'.format(tentativas))
