print('-='*30)
print(f'{'LOJA SUPER BARATÃO':^60}')
print('-='*30)


quantidade = 0
total = 0
produtos_1000 = 0
nome_mais_barato = ''
preco_mais_barato = 0

while True:
    nome = str(input('Informe o nome do produto: '))
    valor = float(input('Informe o valor do produto R$'))

    quantidade += 1
    total += valor

    if valor > 1000:
        produtos_1000 += 1

    if quantidade == 1:
        nome_mais_barato = nome
        preco_mais_barato = valor

    if valor < preco_mais_barato:
        nome_mais_barato = nome
        preco_mais_barato = valor

    continuar = str(input('Quer continuar? (S/N): ')).strip().lower()

    if continuar == 'n':
        break

print(f'O total de compras foi R${total:.2f}')
print(f'Temos {produtos_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} \
custando R${preco_mais_barato:.2f}')
