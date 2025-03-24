def notas(*n, situacao=False):
    """
    Função para calcular a média e situação de vários alunos.

    Args:
        *n (float): Notas dos alunos (aceita múltiplos valores).
        situacao (bool): Opcional para exibição da situação.

    Returns:
        dict: Dicionário com as seguintes informações:
            - 'total' (int): Total de notas.
            - 'maior' (float): Maior nota.
            - 'menor' (float): Menor nota.
            - 'media' (float): Média das notas.
            - 'situacao' (str, optional): Situação da turma (apenas se situacao=True).
    """
    total = len(n)
    maior = max(n)
    menor = min(n)
    media = sum(n) / total

    resultado = { 'total': total, 'maior': maior, 'menor': menor, 'media': media }

    s = ''
    if situacao:
        if media <= 4:
            s = 'RUIM'
        elif media <= 7:
            s = 'RAZOAVEL'
        elif media <= 10:
            s = 'BOA'
        
        resultado['situação'] = s

    return resultado


print(notas(8.5, 9, situacao=True))
print(notas(3.5, 2, 7, 2, 4, situacao=True))
print(notas(6.5, 7, situacao=True))
