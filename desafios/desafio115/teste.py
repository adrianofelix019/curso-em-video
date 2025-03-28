from lib import interface
from time import sleep

while True:
    interface.cabecalho('sistema arquivo v1.0')
    resposta = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        interface.cabecalho('Saindo do Sistema... Até logo.')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
        sleep(2)
