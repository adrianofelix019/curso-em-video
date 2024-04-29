from time import sleep


n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
opcao = 0

while opcao != '5':
    opcao = input('''[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos Números
[ 5 ] - Sair
Opção: ''')

    if opcao == '1':
        print('='*30)
        print('{} + {} = {}'.format(n1, n2, (n1 + n2)))
        print('='*30)

    elif opcao == '2':
        print('='*30)
        print('{} x {} = {}'.format(n1, n2, (n1 * n2)))
        print('='*30)

    elif opcao == '3':
        if n1 > n2:
            print('='*30)
            print('{} é maior que {}'.format(n1, n2))
            print('='*30)
        elif n2 > n1:
            print('='*30)
            print('{} é maior que {}'.format(n2, n1))
            print('='*30)
        else:
            print('='*30)
            print('{} e {} são iguais.'.format(n1, n2))
            print('='*30)

    elif opcao == '4':
        print('='*30)
        print('Informe os novos números.')
        n1 = int(input('Primeiro número:'))
        n2 = int(input('Segundo número:'))
        print('='*30)
    elif opcao == '5':
        print('')
    else:
        print('Opção inválida, tente novamente.')
    sleep(1)
print('Finalizando o programa.')
