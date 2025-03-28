import requests


def acessar(url):
    try:
        response = requests.head(url)

        if response.status_code == 200:
            print('Consegui acessar o site Pudim com sucesso.')
        else:
            print('Não consegui acessar o site Pudim.')
    except requests.ConnectionError:
        print('O site Pudim não está acessivel no momento.')


acessar('https://www.pudim.com.br/')
