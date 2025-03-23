def fatorial(numero, show=False):
    """
    Calcula o Fatorial de um número

    Args:
        numero (int): número a ser calculado
        show (bool): mostrar ou não a conta
    
    Returns:
        int: o fatorial de `numero`
    """
    resultado = 1

    for c in range(numero, 0, -1):
        print(c, end=f'{'' if c == 1 else ' x '}')
        resultado *= c

    print(f' = {resultado}')
    return resultado


print(fatorial(5, True))
