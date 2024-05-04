from random import randint

print('-='*25)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^50}')
print('-='*25)

total_vitorias = 0
while True:
    valor = int(input('Digite um valor: '))
    jogador_par_ou_impar = str(input('Par ou Ímpar [P/I]: ')).strip().lower()
    computador_par_ou_impar = 'i' if jogador_par_ou_impar == 'p' else 'p'
    valor_computador = randint(0, 10)
    total = valor + valor_computador

    print(f'Você jogou {valor} e o computador {valor_computador}', end='')
    print(f', total {total}.')

    if total % 2 == 0:
        print('Deu Par!')

        if jogador_par_ou_impar == 'p':
            total_vitorias += 1
            print('Você venceu!')
            print('Vamos jogar novamente...')
        else:
            print('Você perdeu!')
            break

    else:
        print('Deu Ímpar!')

        if jogador_par_ou_impar == 'i':
            total_vitorias += 1
            print('Você venceu!')
            print('Vamos jogar novamente...')
        else:
            print('Você perdeu!')
            break

print(f'Game Over! Você venceu {total_vitorias} vezes.')
