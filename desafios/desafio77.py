palavras = ('banana', 'carro', 'computador', 'girafa', 'chuva', 
           'montanha', 'guitarra', 'sorriso', 'livro', 'oceano', 
           'aventura', 'futebol', 'lua', 'floresta', 'arco-iris', 
           'viagem', 'castelo', 'chocolate', 'telefone', 'lapis')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')

    ultima_posição_vogal = 0
    for indice, letra in enumerate(palavra):
        if letra.lower() in 'aeiou':
            ultima_posição_vogal = indice

    for indice, letra in enumerate(palavra):
        if letra.lower() in 'aeiou':
            if indice == ultima_posição_vogal:
                print(letra, end='')
            else:
                print(letra, end=', ')
    print()
