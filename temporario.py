import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    # Escolha do computador
    escolha_computador = random.choice(opcoes)

    # Escolha do jogador
    escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    # Verificar se a escolha do jogador é válida
    if escolha_jogador not in opcoes:
        print("Escolha inválida. Escolha pedra, papel ou tesoura.")
        return

    print("Computador escolheu:", escolha_computador)
    print("Jogador escolheu:", escolha_jogador)

    # Verificar quem ganhou
    if escolha_computador == escolha_jogador:
        print("Empate!")
    elif (escolha_computador == 'pedra' and escolha_jogador == 'tesoura') or \
         (escolha_computador == 'papel' and escolha_jogador == 'pedra') or \
         (escolha_computador == 'tesoura' and escolha_jogador == 'papel'):
        print("Computador ganhou!")
    else:
        print("Jogador ganhou!")

# Loop principal do jogo
while True:
    jogar()
    continuar = input("Quer jogar novamente? (s/n): ").lower()
    if continuar != 's':
        break
