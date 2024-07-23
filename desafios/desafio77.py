palavras = ('banana', 'carro', 'computador', 'girafa', 'chuva', 
           'montanha', 'guitarra', 'sorriso', 'livro', 'oceano', 
           'aventura', 'futebol', 'lua', 'floresta', 'arco-íris', 
           'viagem', 'castelo', 'chocolate', 'telefone', 'lápis')

for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()
