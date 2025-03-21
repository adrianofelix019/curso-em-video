def escreva(texto):
    comprimento = len(texto) + 2
    print('~' * comprimento)
    print(f'{texto:^{comprimento}}')
    print('~' * comprimento)



escreva('Curso de Python')
escreva('Git')
escreva('the quick fox jumps over the lazy dog')
