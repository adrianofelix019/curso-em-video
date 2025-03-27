try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('\nO usuário interrompeu o programa.')
finally:
    print('Volte sempre!')
